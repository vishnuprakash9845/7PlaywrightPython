from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("standard_user",timeout=3000)
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    products_header = page.locator("//span[text()='Products']")
    assert products_header.is_visible(), "user is unable to login"

    page.pause()

    burger_menu = page.locator("#react-burger-menu-btn")
    burger_menu.click()

    logout_button = page.locator("//div[@class='bm-menu']//a[text()='Logout']")
    logout_button.click()

    login_button = page.locator("#login-button")
    assert login_button.is_visible(), "user is unable to logout"

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
