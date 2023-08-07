from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

@pytest.mark.regression
def test_get_text(set_up_tear_down) -> None:
    page = set_up_tear_down

    page.locator("#login-button").click()

    error_text = page.locator("//h3[@data-test='error']").inner_text()
    print(error_text)

    page.locator('#user-name').fill("standard_user")
    entered_value = page.locator('#user-name').input_value()
    print(entered_value)

    login_btn = page.locator("#login-button")
    print(login_btn.input_value())

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