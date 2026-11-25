import pytest
import re
from playwright.sync_api import Page, expect
from pages.inventory import InventoryPage
from pages.cart import CartPage

@pytest.mark.smoke
def test_cart_shows_added_items(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_items_to_cart(3)
    inventory_page.open_cart()

    cart = CartPage(logged_in_page)
    expect(cart.title).to_have_text("Your Cart")
    expect(cart.cart_items).to_have_count(3)

def test_cart_items_match_added(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_items_to_cart(2)
    inventory_page.open_cart()

    cart = CartPage(logged_in_page)
    expect(cart.cart_items).to_have_count(2)
    for qty in cart.item_quantities.all_inner_texts():
        assert qty == "1"

def test_remove_item_in_cart(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_items_to_cart(3)
    inventory_page.open_cart()

    cart = CartPage(logged_in_page)
    cart.remove_first_item()
    expect(cart.cart_items).to_have_count(2)
    expect(inventory_page.cart_badge).to_have_text("2")

def test_continue_shopping_returns_to_inventory(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.open_cart()
    CartPage(logged_in_page).continue_shopping()
    expect(logged_in_page).to_have_url(re.compile(r"inventory\.html"))