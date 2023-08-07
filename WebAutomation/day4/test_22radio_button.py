from playwright.sync_api import Page, sync_playwright, expect
import time

def test_get_text(page: Page) -> None:
    page.goto("https://artoftesting.com/samplesiteforselenium")
    time.sleep(1)
    #page.locator("//input[@type='checkbox' and contains(@value,'Automation')]").check()
    page.locator(get_days_radiobutton("male")).check()
    page.wait_for_timeout(3000)
    assert page.locator(get_days_radiobutton("male")).is_checked()
    time.sleep(1)
    page.locator(get_days_radiobutton("female")).check()
    time.sleep(1)
    assert not page.locator(get_days_radiobutton("male")).is_checked()
    time.sleep(1)

def get_days_radiobutton(valu):
    return f"//input[@type='radio' and @value='{valu}']"