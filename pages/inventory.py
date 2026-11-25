from playwright.sync_api import Page
class InventoryPage:

    def __init__(self, page: Page):
        self.page = page
        self.burger_menu = page.locator("#react-burger-menu-btn")
        self.all_items_link = page.locator("#inventory_sidebar_link")
        self.dynamic_catalog_link = page.locator("#dynamic_catalog_sidebar_link")
        self.about_link = page.locator("#about_sidebar_link")
        self.logout_link = page.locator("#logout_sidebar_link")
        self.reset_app_state = page.locator("#reset_sidebar_link")
        self.bm_close_icon = page.locator("#react-burger-cross-btn")
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")
        self.item_names = page.locator("[data-test='inventory-item-name']")
        self.item_prices = page.locator("[data-test='inventory-item-price']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.add_to_cart_buttons = page.locator("[data-test^='add-to-cart']")
        self.remove_buttons = page.locator("[data-test^='remove']")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")
        self.menu = page.locator(".bm-menu-wrap")

    def open_menu(self):
        self.burger_menu.click()

    def close_menu(self):
        self.bm_close_icon.click()

    def sort_by(self, option_value: str):
        self.sort_dropdown.select_option(option_value)

    def get_item_names(self):
        return self.item_names.all_inner_texts()

    def get_item_prices(self):
        texts = self.item_prices.all_inner_texts()
        return [float(t.replace("$", "")) for t in texts]

    def add_items_to_cart(self, count: int):
        for _ in range(count):
            self.add_to_cart_buttons.first.click()

    def remove_first_item(self):
        self.remove_buttons.first.click()

    def remove_all_items(self):
        while self.remove_buttons.count() > 0:
            self.remove_buttons.first.click()

    def open_item_by_name(self, name: str):
        self.page.get_by_text(name, exact=True).click()

    def open_cart(self):
        self.cart_link.click()