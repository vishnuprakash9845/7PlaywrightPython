from playwright.sync_api import Page, sync_playwright, expect
import time

def test_get_text(page: Page) -> None:
    page.goto("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")
    time.sleep(1)
    #page.locator("//select[@id='second']").select_option(['pizza','bonda'])
    #page.locator("//select[@id='second']").select_option(['Donut','Burger'],label='Bonda')
    page.locator("//select[@id='second']").select_option(index=1,value='bonda',label='Pizza')
    page.wait_for_timeout(3000)
    page.locator("//select[@id='second']").select_option(index=1,value='bonda')
    time.sleep(1)

def get_days_radiobutton(valu):
    return f"//input[@type='radio' and @value='{valu}']"