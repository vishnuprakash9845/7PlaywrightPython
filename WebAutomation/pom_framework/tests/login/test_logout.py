from playwright.sync_api import Page, expect
import pytest

def test_logout(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    page.locator("#react-burger-menu-btn").click()
    page.locator("//div[@class='bm-menu']//a[text()='Logout']").click()
    login_button = page.locator("#login-button")
    expect(login_button).to_be_visible()
    expect(page.get_by_text("Login")).to_be_visible()