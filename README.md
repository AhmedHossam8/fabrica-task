# Customer Visits

A Frappe/ERPNext app for scheduling and managing customer visits.

## Features

- Create and manage Customer Visit Requests linked to ERPNext Customers
- Workflow-based approval process (Draft → Approved → Completed / Rejected / Cancelled)
- Enforces one active visit request per customer at a time
- Automatically updates the customer's Last Visit Date when a visit is completed
- Automatically cancels active visit requests when a customer's territory changes
- Adds a custom button on the Customer form to create or view visit requests

## Requirements

- Frappe Framework v15
- ERPNext v15

## Installation

Using the [bench](https://github.com/frappe/bench) CLI:
```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench --site your-site-name install-app customer_visits
bench --site your-site-name migrate
```

## Workflow States

| State     | Description                              |
|-----------|------------------------------------------|
| Draft     | Visit request created, pending approval  |
| Approved  | Visit request approved, visit scheduled  |
| Completed | Visit has taken place                    |
| Rejected  | Visit request was rejected               |
| Cancelled | Visit request was cancelled              |

## Workflow Transitions

| From     | Action   | To        | Role           |
|----------|----------|-----------|----------------|
| Draft    | Approve  | Approved  | System Manager |
| Draft    | Reject   | Rejected  | System Manager |
| Approved | Complete | Completed | System Manager |
| Approved | Cancel   | Cancelled | System Manager |

## Business Rules

- **One active visit per customer** — a customer can only have one visit request in Draft or Approved state at a time. Attempting to create a second will throw a validation error.
- **Last Visit Date** — when a visit request is moved to Completed, the linked customer's `custom_last_visit_date` field is automatically updated with the visit date.
- **Territory change** — if a customer's territory is changed, all their active (Draft or Approved) visit requests are automatically cancelled.

## Custom Fields

| DocType  | Field                  | Type | Description                              |
|----------|------------------------|------|------------------------------------------|
| Customer | custom_last_visit_date | Date | Auto-updated when a visit is completed   |

## Customer Form Buttons

On the Customer form, a dynamic button is shown:
- **Create Visit Request** — if no active visit request exists
- **View Scheduled Visit Request** — if a Draft or Approved visit request exists, clicking navigates directly to it

## Contributing

This app uses `pre-commit` for code formatting and linting. Install and enable it:
```bash
cd apps/customer_visits
pre-commit install
```

Tools used:
- **ruff** — Python linting and formatting
- **eslint** — JavaScript linting
- **prettier** — JavaScript/Vue/SCSS formatting

## License

MIT
