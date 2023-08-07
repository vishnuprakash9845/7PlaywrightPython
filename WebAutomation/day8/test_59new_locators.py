from playwright.sync_api import Page, sync_playwright, expect
import time

def test_new_locators(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    username = page.get_by_placeholder("Username")
    password = page.get_by_placeholder("Password")
    login_btn = page.get_by_text("Login")

    username.fill("standard_user")
    password.fill("secret_sauce")
    login_btn.click()

def test_new_locator_api2(page: Page) -> None:
    page.goto("https://www.google.com")
    page.get_by_title("Search").fill("Playwright")
    page.get_by_role("button",name="Google Search").nth(0).click()
    time.sleep(3)

def test_new_locator_api3(page: Page) -> None:
    page.goto("https://demo.opencart.com/index.php?route=product/product&language=en-gb&product_id=40")
    quantity = page.get_by_label("Qty")
    expect(quantity).to_be_visible()
    time.sleep(2)

    #

    # pytest -s -v --headed .\test_59new_locators.py --slowmo=1000 --html=myreport.html --capture=tee-sys
    # pytest -s -v --headed .\test_59new_locators.py::test_new_locator_api2