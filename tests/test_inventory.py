from pages.inventory import InventoryPage
from playwright.sync_api import Page, expect

import re
def test_burger_menu_links(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)

    expect(inventory_page.all_items_link).to_be_visible()
    expect(inventory_page.dynamic_catalog_link).to_be_visible()
    expect(inventory_page.about_link).to_be_visible()
    expect(inventory_page.logout_link).to_be_visible()
    expect(inventory_page.reset_app_state).to_be_visible()

def test_burger_menu_closes(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.open_menu()
    inventory_page.close_menu()

def test_sort_name_z_to_a(logged_in_page: Page):
    inv = InventoryPage(logged_in_page)
    before = inv.get_item_names()
    inv.sort_by("za")
    expect(inv.item_names).not_to_have_text(before)
    names = inv.get_item_names()
    assert names == sorted(names, reverse=True)

def test_sort_name_a_to_z(logged_in_page: Page):
    inv = InventoryPage(logged_in_page)
    inv.sort_by("za")
    before = inv.get_item_names()
    inv.sort_by("az")
    expect(inv.item_names).not_to_have_text(before)
    names = inv.get_item_names()
    assert names == sorted(names)

def test_sort_price_low_to_high(logged_in_page: Page):
    inv = InventoryPage(logged_in_page)
    before = inv.get_item_names()
    inv.sort_by("lohi")
    expect(inv.item_names).not_to_have_text(before)
    prices = inv.get_item_prices()
    assert prices == sorted(prices)

def test_sort_price_high_to_low(logged_in_page: Page):
    inv = InventoryPage(logged_in_page)
    before = inv.get_item_names()
    inv.sort_by("hilo")
    expect(inv.item_names).not_to_have_text(before)
    prices = inv.get_item_prices()
    assert prices == sorted(prices, reverse=True)

def test_cart_badge_one_item(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_items_to_cart(1)
    expect(inventory_page.cart_badge).to_have_text("1")

def test_cart_badge_three_items(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_items_to_cart(3)
    expect(inventory_page.cart_badge).to_have_text("3")
    expect(inventory_page.remove_buttons).to_have_count(3)

def test_cart_badge_decreases_on_remove(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_items_to_cart(3)
    inventory_page.remove_first_item()
    expect(inventory_page.cart_badge).to_have_text("2")

def test_cart_badge_hidden_when_empty(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    expect(inventory_page.cart_badge).to_have_count(0)

def test_remove_button_returns_to_add_to_cart(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_items_to_cart(1)
    inventory_page.remove_first_item()
    expect(inventory_page.remove_buttons).to_have_count(0)
    expect(inventory_page.add_to_cart_buttons).to_have_count(6)

def test_badge_disappears_when_all_removed(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_items_to_cart(3)
    inventory_page.remove_all_items()
    expect(inventory_page.cart_badge).to_have_count(0)

from pages.product_details import ProductDetailsPage

def test_open_backpack_details(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.open_item_by_name("Sauce Labs Backpack")

    details = ProductDetailsPage(logged_in_page)
    expect(logged_in_page).to_have_url(re.compile(r"inventory-item\.html\?id=4"))
    expect(details.item_name).to_have_text("Sauce Labs Backpack")
    expect(details.item_price).to_have_text("$29.99")

def test_back_to_products(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.open_item_by_name("Sauce Labs Backpack")
    ProductDetailsPage(logged_in_page).go_back()
    expect(logged_in_page).to_have_url(re.compile(r"inventory\.html"))

def test_details_price_matches_list(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    list_price = inventory_page.get_item_prices()[0]
    first_name = inventory_page.get_item_names()[0]

    inventory_page.open_item_by_name(first_name)
    details = ProductDetailsPage(logged_in_page)
    expect(details.item_price).to_have_text(f"${list_price}")