from playwright.sync_api import Page, sync_playwright, expect
import time

def test_get_text(page: Page) -> None:
    page.goto("https://git-scm.com/docs/git-push")
    time.sleep(1)
    # download_link=page.locator("a",has_text="Downloads")
    # download_link.click()
    # page.wait_for_timeout(3000)

    four_elements = page.locator("ul.expanded",has=page.locator("a",has_text="Reference"))
    texts = four_elements.all_inner_texts()
    print(texts)

    time.sleep(5)