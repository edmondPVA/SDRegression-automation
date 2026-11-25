from playwright.sync_api import Page

class CheckoutInfoPage:

    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator("[data-test='title']")
        self.first_name = page.locator("[data-test='firstName']")
        self.last_name = page.locator("[data-test='lastName']")
        self.postal_code = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        self.cancel_button = page.locator("[data-test='cancel']")
        self.error = page.locator("[data-test='error']")

    def fill_info(self, first: str, last: str, postal: str):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(postal)

    def continue_to_overview(self):
        self.continue_button.click()

    def cancel(self):
        self.cancel_button.click()

class CheckoutOverviewPage:

    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator("[data-test='title']")
        self.item_names = page.locator("[data-test='inventory-item-name']")
        self.item_prices = page.locator("[data-test='inventory-item-price']")
        self.subtotal_label = page.locator("[data-test='subtotal-label']")
        self.tax_label = page.locator("[data-test='tax-label']")
        self.total_label = page.locator("[data-test='total-label']")
        self.finish_button = page.locator("[data-test='finish']")
        self.cancel_button = page.locator("[data-test='cancel']")

    @staticmethod
    def _amount(text: str) -> float:
        return float(text.split("$")[-1])

    def get_item_prices(self):
        return [self._amount(t) for t in self.item_prices.all_inner_texts()]

    def get_subtotal(self):
        return self._amount(self.subtotal_label.inner_text())

    def get_tax(self):
        return self._amount(self.tax_label.inner_text())

    def get_total(self):
        return self._amount(self.total_label.inner_text())

    def finish(self):
        self.finish_button.click()

class CheckoutCompletePage:

    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator("[data-test='title']")
        self.complete_header = page.locator("[data-test='complete-header']")
        self.complete_text = page.locator("[data-test='complete-text']")
        self.back_home_button = page.locator("[data-test='back-to-products']")

    def back_to_products(self):
        self.back_home_button.click()