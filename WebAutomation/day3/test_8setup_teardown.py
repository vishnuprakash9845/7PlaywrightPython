from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

@pytest.mark.regression
def test_login_with_valid_credentails(set_up) -> None:
    page = set_up

    page.locator("#user-name").fill("standard_user",timeout=3000)
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    products_header = page.locator("//span[text()='Products']")
    assert products_header.is_visible(), "user is unable to login"

    burger_menu = page.locator("#react-burger-menu-btn")
    burger_menu.click()

def test_logout(set_up) -> None:
    page = set_up
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

@pytest.mark.sanity
def test_App_launch(set_up) -> None:
    page = set_up
    page.locator("#user-name").fill("standard_user",timeout=3000)
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

