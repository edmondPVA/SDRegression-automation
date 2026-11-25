from playwright.sync_api import Page
class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator("[data-test='title']")
        self.cart_items = page.locator("[data-test='inventory-item']")
        self.item_names = page.locator("[data-test='inventory-item-name']")
        self.item_prices = page.locator("[data-test='inventory-item-price']")
        self.item_quantities = page.locator("[data-test='item-quantity']")
        self.remove_buttons = page.locator("[data-test^='remove']")
        self.continue_shopping_button = page.locator("[data-test='continue-shopping']")
        self.checkout_button = page.locator("[data-test='checkout']")
        self.error = page.locator("[data-test='error']")

    def remove_first_item(self):
        self.remove_buttons.first.click()

    def continue_shopping(self):
        self.continue_shopping_button.click()

    def go_to_checkout(self):
        self.checkout_button.click()

    def get_item_names(self):
        return self.item_names.all_inner_texts()