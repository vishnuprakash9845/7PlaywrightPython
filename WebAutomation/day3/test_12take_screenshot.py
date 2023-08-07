from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

@pytest.mark.regression
def test_login_with_valid_credentails(set_up_tear_down) -> None:
    page = set_up_tear_down

    page.locator("#user-name").fill("standard_user",timeout=3000)
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    products_header = page.locator("//span[text()='Products']")
    assert products_header.is_visible(), "user is unable to login"

    burger_menu = page.locator("#react-burger-menu-btn")
    burger_menu.click()

def test_logout(set_up_tear_down) -> None:
    page = set_up_tear_down
    page.locator("#user-name").fill("standard_user",timeout=3000)
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    products_header = page.locator("//span[text()='Products']")
    assert products_header.is_visible(), "user is unable to login"

    #page.screenshot(path="Screenshots/screenshot.png", full_page=True)
    page.screenshot(path="Screenshots/screenshot.png")

    burger_menu = page.locator("#react-burger-menu-btn")
    burger_menu.click()

    logout_button = page.locator("//div[@class='bm-menu']//a[text()='Logout']")
    logout_button.click()

    login_button = page.locator("#login-button")
    assert login_button.is_visible(), "user is unable to logout" 

@pytest.mark.regression
def test_login_with_invalid_credentails(set_up_tear_down) -> None:
    page = set_up_tear_down

    page.locator("#user-name").fill("standard_user",timeout=3000)
    page.locator("#password").fill("secret_sauce1")
    page.locator("#login-button").click()

    error_Text = page.locator("//div[@class='error-message-container error']/h3")
    error_Text.wait_for()
    print(error_Text.inner_text())

    actual_errortext = "Username and password do not match any user in this service"

    assert actual_errortext in error_Text.inner_text(), "Correct error message is not displayed"