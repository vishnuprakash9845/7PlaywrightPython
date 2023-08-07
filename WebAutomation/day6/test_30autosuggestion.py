from playwright.sync_api import Page, sync_playwright, expect
import time

def test_autosuggestion(page: Page) -> None:
    page.goto("https://weboverhauls.github.io/demos/autosuggest/")
    #page.wait_for_timeout(5000)

    subject_input = page.locator("//input[@id='search']")
    subject_input.click()
    subject_input.fill("wa")
    time.sleep(2)
    auto_suggestions = page.locator("div#search-autocomplete ul#res li")
    print(auto_suggestions)
    index=0
    while index < auto_suggestions.count():
        print(auto_suggestions.nth(index).inner_text())
        if auto_suggestions.nth(index).inner_text()=='Washington':
            auto_suggestions.nth(index).click()
        index = index+1

    page.wait_for_timeout(3000)

    #time.sleep(3)

