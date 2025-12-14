# Invoice Dashboard

Invoice Dashboard is a small Python project for summarizing invoice data. It loads invoice records from JSON and prints a human-friendly dashboard that highlights totals, outstanding balances, and overdue invoices.

## Features
- Load invoices from a JSON file.
- Provide totals for issued, paid, and outstanding invoices.
- Highlight overdue invoices with details and customer breakdowns.
- Export summaries to a JSON report for further processing.

## Quickstart
1. Ensure Python 3.10+ is available.
2. Install the project in editable mode:

```bash
cd Invoice-Dashboard
pip install -e .
```

3. Run the dashboard against the sample data:

```bash
invoice-dashboard data/invoices.json
```

4. Write an exportable summary to disk:

```bash
invoice-dashboard data/invoices.json --export summary.json
```

## Data format
Invoices are stored as a list of objects with the following fields:

```json
{
  "id": "INV-1001",
  "customer": "Acme Corp",
  "amount": 1250.0,
  "status": "paid",
  "issued_on": "2024-09-01",
  "due_on": "2024-09-15",
  "paid_on": "2024-09-10"
}
```

- `status` should be `paid`, `open`, or `overdue`.
- `paid_on` is optional and only relevant for paid invoices.

## Development
Run the lightweight tests:

```bash
pytest
```

## License
This project is licensed under the MIT License.
