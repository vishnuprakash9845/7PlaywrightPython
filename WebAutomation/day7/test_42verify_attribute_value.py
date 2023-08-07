from playwright.sync_api import Page, sync_playwright, expect
import time

def test_field_editable(page: Page) -> None:
    page.goto("https://saucedemo.com")
    user_name = page.locator("id=user-name")
    user_name.fill("standard_user")
    pass_word = page.locator("id=password")
    pass_word.fill("dsfdsf")
    login_btn = page.locator("id=login-button")
    login_btn.click()

    error_msg = page.locator("data-test=error")
    expect(error_msg).to_contain_text("Username and password do not match")
    expect(error_msg).not_to_have_text("Test")
    expect(user_name).to_have_attribute('placeholder','Username')
    expect(pass_word).to_have_attribute('placeholder','Password')
    time.sleep(1)

#pytest -s -v --headed .\test_42verify_attribute_value.py