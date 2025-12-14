from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable, List, Tuple


@dataclass
class Invoice:
    id: str
    customer: str
    amount: float
    status: str
    issued_on: date
    due_on: date
    paid_on: date | None = None

    @classmethod
    def from_mapping(cls, payload: dict) -> "Invoice":
        return cls(
            id=str(payload["id"]),
            customer=payload["customer"],
            amount=float(payload["amount"]),
            status=payload["status"],
            issued_on=_parse_date(payload["issued_on"]),
            due_on=_parse_date(payload["due_on"]),
            paid_on=_parse_date(payload.get("paid_on")) if payload.get("paid_on") else None,
        )

    def is_paid(self) -> bool:
        return self.status.lower() == "paid"

    def is_overdue(self, today: date | None = None) -> bool:
        if self.status.lower() == "overdue":
            return True
        if today is None:
            return False
        return self.status.lower() != "paid" and self.due_on < today


@dataclass
class DashboardSummary:
    total_invoices: int
    total_amount: float
    paid_amount: float
    outstanding_amount: float
    overdue_invoices: List[Invoice]
    customers: List[Tuple[str, float]]

    def to_dict(self) -> dict:
        return {
            "total_invoices": self.total_invoices,
            "total_amount": self.total_amount,
            "paid_amount": self.paid_amount,
            "outstanding_amount": self.outstanding_amount,
            "overdue_count": len(self.overdue_invoices),
            "overdue_invoices": [invoice.id for invoice in self.overdue_invoices],
            "customers": self.customers,
        }


def _parse_date(value: str) -> date:
    return date.fromisoformat(value)


def load_invoices(path: Path) -> List[Invoice]:
    with path.open() as handle:
        raw = json.load(handle)
    return [Invoice.from_mapping(item) for item in raw]


def summarize_invoices(invoices: Iterable[Invoice]) -> DashboardSummary:
    invoices_list = list(invoices)
    total_amount = sum(invoice.amount for invoice in invoices_list)
    paid_amount = sum(invoice.amount for invoice in invoices_list if invoice.is_paid())
    outstanding_amount = total_amount - paid_amount

    overdue = [invoice for invoice in invoices_list if invoice.is_overdue()]
    customer_totals = _aggregate_by_customer(invoices_list)

    return DashboardSummary(
        total_invoices=len(invoices_list),
        total_amount=total_amount,
        paid_amount=paid_amount,
        outstanding_amount=outstanding_amount,
        overdue_invoices=overdue,
        customers=customer_totals,
    )


def _aggregate_by_customer(invoices: Iterable[Invoice]) -> List[Tuple[str, float]]:
    totals: dict[str, float] = {}
    for invoice in invoices:
        totals[invoice.customer] = totals.get(invoice.customer, 0.0) + invoice.amount
    return sorted(totals.items(), key=lambda item: item[1], reverse=True)


def print_dashboard(summary: DashboardSummary) -> None:
    print("Invoice Dashboard")
    print("================")
    print(f"Total invoices: {summary.total_invoices}")
    print(f"Total amount:   ${summary.total_amount:,.2f}")
    print(f"Paid amount:    ${summary.paid_amount:,.2f}")
    print(f"Outstanding:    ${summary.outstanding_amount:,.2f}")
    print()
    if summary.overdue_invoices:
        print("Overdue Invoices:")
        for invoice in summary.overdue_invoices:
            print(
                f"- {invoice.id} for {invoice.customer}: ${invoice.amount:,.2f} "
                f"(due {invoice.due_on.isoformat()})"
            )
        print()
    else:
        print("No overdue invoices.\n")

    print("Top customers by amount:")
    for customer, total in summary.customers:
        print(f"- {customer}: ${total:,.2f}")


def main(argv: List[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Summarize invoice data")
    parser.add_argument("path", type=Path, help="Path to the invoices JSON file")
    parser.add_argument("--export", type=Path, help="Optional path to write JSON summary")
    args = parser.parse_args(argv)

    invoices = load_invoices(args.path)
    summary = summarize_invoices(invoices)

    print_dashboard(summary)

    if args.export:
        args.export.write_text(json.dumps(summary.to_dict(), indent=2))


if __name__ == "__main__":
    main()
