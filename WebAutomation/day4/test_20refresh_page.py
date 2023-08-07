from playwright.sync_api import Page, sync_playwright, expect
import time

def test_get_text(page: Page) -> None:
    page.goto("https://www.amazon.in/")
    time.sleep(3)
    page.reload(timeout=0)
    time.sleep(3)