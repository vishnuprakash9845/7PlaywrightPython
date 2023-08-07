from playwright.sync_api import Page, sync_playwright, expect
import time

def test_click_for_js_alert(page: Page) -> None:
    page.goto("http://uitestingplayground.com/ajax")

    button = page.locator("text=Button Triggering AJAX Request")
    button.click()

    final_msg = page.locator("p.bg-success").inner_text(timeout=16000)
    print(final_msg)

    time.sleep(1)