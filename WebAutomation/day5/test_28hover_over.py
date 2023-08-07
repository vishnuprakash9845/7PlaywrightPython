from playwright.sync_api import Page, sync_playwright, expect
import time

def test_get_text(page: Page) -> None:
    page.goto("https://www.globalsqa.com/demo-site/")
    time.sleep(1)

    header_menu = page.locator("#menu-item-7128",has_text="Free Ebooks")

    print(header_menu.text_content())
    print(header_menu.count())
    header_menu.hover()
    page.wait_for_timeout(3000)
    time.sleep(3)