# SDRegression-automation

Automated UI regression suite for [SauceDemo](https://www.saucedemo.com), built with **Playwright** and **pytest** in Python using the **Page Object Model (POM)**.

## Tech stack

- Python 3.14
- Playwright (via `pytest-playwright`)
- pytest (fixtures, parametrization, markers)
- Firefox as the default browser

## What's covered (31 tests)

| Area | File | What it checks |
|---|---|---|
| Login | `tests/test_login.py` | Page loads, valid login, empty fields, wrong credentials, locked-out user |
| Inventory | `tests/test_inventory.py` | Burger menu, sorting (A–Z, Z–A, price low/high), cart badge, add/remove, product details |
| Cart | `tests/test_cart.py` | Added items appear, quantities, removing items, continue shopping |
| Checkout | `tests/test_checkout.py` | Required-field validation, full checkout through to order confirmation |

## Project structure

```
SDRegression-automation/
├── pages/            # Page objects: locators + actions for each screen
│   ├── login.py
│   ├── inventory.py
│   ├── product_details.py
│   ├── cart.py
│   └── checkout.py
├── tests/            # Test cases, grouped by feature
├── conftest.py       # Shared fixtures (login, logged-in page, checkout setup)
├── pytest.ini        # Base URL, browser, reporting and marker settings
└── requirements.txt
```

## Setup

```bash
git clone https://github.com/edmondPVA/SDRegression-automation.git
cd SDRegression-automation
python -m venv venv
venv\Scripts\activate          # Windows  (macOS/Linux: source venv/bin/activate)
pip install -r requirements.txt
playwright install firefox
```

## Running the tests

```bash
pytest                         # full suite
pytest tests/test_cart.py      # one feature
pytest -m smoke                # quick sanity checks only
pytest --headed                # watch the browser while tests run
```

## Reports and debugging

On a failed test, Playwright keeps a **trace**, a **screenshot** and a **video** in `reports/artifacts/`. A JUnit XML report is written to `reports/junit.xml`.

To step through a failed run:

```bash
playwright show-trace reports/artifacts/<test-name>/trace.zip
```

## Author

**Edmond Polinar** · QA / Virtual Assistant
[LinkedIn](https://www.linkedin.com/in/edmond-polinar-957346413/) · [GitHub](https://github.com/edmondPVA)
