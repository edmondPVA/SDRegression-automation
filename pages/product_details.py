from playwright.sync_api import Page
class ProductDetailsPage:

    def __init__(self, page: Page):
        self.page = page
        self.item_name = page.locator("[data-test='inventory-item-name']")
        self.item_desc = page.locator("[data-test='inventory-item-desc']")
        self.item_price = page.locator("[data-test='inventory-item-price']")
        self.add_to_cart_button = page.locator("[data-test^='add-to-cart']")
        self.back_button = page.locator("[data-test='back-to-products']")

    def go_back(self):
        self.back_button.click()


