import re
import pytest
from playwright.sync_api import expect
from pages.login import LoginPage
from pages.inventory import InventoryPage
from pages.cart import CartPage
from pages.checkout import CheckoutInfoPage

USERNAME, PASSWORD = "standard_user", "secret_sauce"

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):

    return {**browser_type_launch_args, "firefox_user_prefs": {
        "network.trr.mode": 3,
        "network.trr.uri": "https://mozilla.cloudflare-dns.com/dns-query",
        "network.trr.bootstrapAddr": "1.1.1.1",
    }}

@pytest.fixture
def login_page(page):
    page.goto("/")
    return LoginPage(page)

@pytest.fixture
def logged_in_page(page, login_page):
    login_page.enter_account(USERNAME, PASSWORD)
    expect(page).to_have_url(re.compile(r"inventory\.html"))
    return page

@pytest.fixture
def checkout_info_page(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_items_to_cart(2)
    inventory.open_cart()
    CartPage(logged_in_page).go_to_checkout()
    return CheckoutInfoPage(logged_in_page)