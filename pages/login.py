from playwright.sync_api import Page
class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.login_container = page.locator(".login_wrapper-inner")
        self.error = page.locator("[data-test='error']")

    def enter_account(self, first: str, second: str,):
        self.username.fill(first)
        self.password.fill(second)
        self.login_button.click()

    def empty_entry(self):
        self.username.focus()
        self.username.blur()
        self.password.focus()
        self.password.blur()
        self.login_button.click()