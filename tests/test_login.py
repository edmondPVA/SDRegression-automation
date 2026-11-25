from environment import base_url
from pages.login import LoginPage
from playwright.sync_api import Page, expect
import pytest

@pytest.mark.smoke
def test_elements_visible(page: Page):
    page.goto(base_url)
    login_page = LoginPage(page)
    expect(login_page.login_container).to_be_visible()
    login_page.login_container.screenshot(path="screenshots/login/login_container.png")

def test_empty_entry(page: Page):
    page.goto(base_url)
    login_page = LoginPage(page)
    login_page.empty_entry()
    expect(page.get_by_text("Epic sadface: Username is required")).to_be_visible()

@pytest.mark.smoke
def test_valid_account(page: Page):
    page.goto(base_url)
    login_page = LoginPage(page)
    login_page.enter_account("standard_user","secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

@pytest.mark.parametrize("user, pwd, message", [
    ("", "secret_sauce", "Username is required"),
    ("standard_user", "", "Password is required"),
    ("normal_user", "secret_password", "Username and password do not match"),
    ("locked_out_user", "secret_sauce", "this user has been locked out"),
], ids=["no-username", "no-password", "wrong-credentials", "locked-out"])

def test_login_errors(page: Page, user, pwd, message):
    page.goto(base_url)
    login_page = LoginPage(page)
    login_page.enter_account(user, pwd)
    expect(login_page.error).to_contain_text(message)