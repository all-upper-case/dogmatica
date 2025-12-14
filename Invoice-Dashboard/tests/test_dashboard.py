from pathlib import Path

from invoice_dashboard.dashboard import load_invoices, summarize_invoices


def test_summarize_sample_data():
    sample_path = Path(__file__).parent.parent / "data" / "invoices.json"
    invoices = load_invoices(sample_path)

    summary = summarize_invoices(invoices)

    assert summary.total_invoices == 4
    assert summary.total_amount == 4980.5
    assert summary.paid_amount == 1250
    assert summary.outstanding_amount == 3730.5
    assert len(summary.overdue_invoices) == 1
    assert summary.overdue_invoices[0].id == "INV-1003"
    assert summary.customers[0][0] == "Initech"
