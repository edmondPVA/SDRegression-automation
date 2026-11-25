import pytest
from playwright.sync_api import Page, expect
from pages.checkout import CheckoutOverviewPage, CheckoutCompletePage

def test_checkout_info_page_loads(checkout_info_page):
    expect(checkout_info_page.title).to_have_text("Checkout: Your Information")

@pytest.mark.parametrize("first, last, postal, message", [
    ("", "Tester", "1000", "First Name is required"),
    ("Jane", "", "1000", "Last Name is required"),
    ("Jane", "Tester", "", "Postal Code is required"),
], ids=["no-first-name", "no-last-name", "no-postal-code"])
def test_checkout_required_fields(checkout_info_page, first, last, postal, message):
    checkout_info_page.fill_info(first, last, postal)
    checkout_info_page.continue_to_overview()
    expect(checkout_info_page.error).to_contain_text(message)

def test_complete_checkout(logged_in_page: Page, checkout_info_page):
    checkout_info_page.fill_info("Jane", "Tester", "1000")
    checkout_info_page.continue_to_overview()
    CheckoutOverviewPage(logged_in_page).finish()
    complete = CheckoutCompletePage(logged_in_page)
    expect(complete.complete_header).to_have_text("Thank you for your order!")