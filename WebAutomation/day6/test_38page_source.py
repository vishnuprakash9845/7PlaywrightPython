from playwright.sync_api import Page, sync_playwright, expect
import time

def test_pagesource(page: Page) -> None:
    page.goto("https://www.google.com/")
    print(page.content())
    print(page.title())