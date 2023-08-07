from playwright.sync_api import Page, sync_playwright, expect
import time

def test_get_text(page: Page) -> None:
    page.goto("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")
    time.sleep(1)
    dropdownoptions = page.locator("//select[@id='first']/option")
    print(dropdownoptions.all_inner_texts())
    print(dropdownoptions.count())
    page.wait_for_timeout(3000)
    index=0
    while index < dropdownoptions.count():
        print(dropdownoptions.nth(index).inner_text())
        index=index+1
    time.sleep(1)