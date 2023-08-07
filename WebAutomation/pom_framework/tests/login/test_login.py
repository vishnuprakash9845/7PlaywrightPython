from playwright.sync_api import Page, expect
from pom_framework.pages.LoginPage import LoginPage
#import pom_framework.pages.LoginPage as LoginPage


def test_login_with_standard_user(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'username':'standard_user','password':'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    expect(products_p.product_header).to_have_text("Products")
    
    # page.goto("https://www.saucedemo.com/")
    # page.locator("#user-name").fill("standard_user")
    # page.locator("#password").fill("secret_sauce")
    # page.locator("#login-button").click()
    # products_header = page.locator("span.title")
    # expect(products_header).to_have_text("Products")

# def test_login_with_invalid_user(page: Page) -> None:
#     page.goto("https://www.saucedemo.com/")
#     page.locator("#user-name").fill("invalid_user")
#     page.locator("#password").fill("secret_sauce")
#     page.locator("#login-button").click()
#     expected_fail_message = "Username and password do not match any user in this service"
#     error_msg_locator = page.locator("//div[@class='error-message-container error']/h3")
#     expect(error_msg_locator).to_contain_text(expected_fail_message)

# def test_login_with_no_credentials(page: Page) -> None:
#     page.goto("https://www.saucedemo.com/")
#     page.locator("#user-name").fill("")
#     page.locator("#password").fill("secret_sauce")
#     page.locator("#login-button").click()
#     expected_fail_message = "Username is required"
#     error_msg_locator = page.locator("//div[@class='error-message-container error']/h3")
#     expect(error_msg_locator).to_contain_text(expected_fail_message)

