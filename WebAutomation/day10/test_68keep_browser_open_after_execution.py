from playwright.sync_api import Page, sync_playwright, expect
import time

def test_keep_browser_open_after_execution(page: Page) -> None:
    page.goto("https://admirhodzic.github.io/multiselect-dropdown/demo.html")
    #page.wait_for_timeout(5000)
    time.sleep(1)
    subject_input = page.locator("select#field1~div:nth-of-type(1)")
    subject_input.click()
    time.sleep(1)
    auto_suggestions = page.locator("select#field1~div:nth-of-type(1) div.multiselect-dropdown-list label")
    print(auto_suggestions)
    auto_suggestions.first.click()
    page.wait_for_timeout(1000)
    auto_suggestions.last.click()
    page.wait_for_timeout(1000)
    page.pause()

    #time.sleep(3)
    # pytest -s -v --headed .\test_68keep_browser_open_after_execution.py

