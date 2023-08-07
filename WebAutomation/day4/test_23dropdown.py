from playwright.sync_api import Page, sync_playwright, expect
import time

def test_get_text(page: Page) -> None:
    page.goto("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")
    time.sleep(1)
    page.locator("//select[@id='first']").select_option(index=2)
    page.locator("//select[@id='first']").select_option(value="Yahoo")
    page.locator("//select[@id='first']").select_option(label="Google")
    page.wait_for_timeout(3000)
    page.locator("//select[@id='first']").select_option("")
    time.sleep(1)

def get_days_radiobutton(valu):
    return f"//input[@type='radio' and @value='{valu}']"