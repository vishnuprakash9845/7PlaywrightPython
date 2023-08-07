from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

@pytest.mark.xfail(reason="BUG 1726")
def test_login_with_valid_credentails(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("standard_user",timeout=3000)
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    products_header = page.locator("//span[text()='Products']")
    assert products_header.is_visible(), "user is unable to login"

    burger_menu = page.locator("#react-burger-menu-btn")
    burger_menu.click()

    # ---------------------
    context.close()
    browser.close()

@pytest.mark.skip(reason="Not implemented")
def test_logout(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("standard_user",timeout=3000)
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    products_header = page.locator("//span[text()='Products']")
    assert products_header.is_visible(), "user is unable to login"

    burger_menu = page.locator("#react-burger-menu-btn")
    burger_menu.click()

    logout_button = page.locator("//div[@class='bm-menu']//a[text()='Logout']")
    logout_button.click()

    login_button = page.locator("#login-button")
    assert login_button.is_visible(), "user is unable to logout"

    # ---------------------
    context.close()
    browser.close()
