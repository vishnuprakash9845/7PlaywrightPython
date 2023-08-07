from playwright.sync_api import Page, sync_playwright, expect
import time
import os

def test_download_file(page: Page) -> None:
    page.goto('https://books-pwakit.appspot.com/')
    page.locator('#input').fill('Science')
    page.keyboard.press('Enter')
    expect(page.locator('text=What is Science?')).to_be_visible()
    time.sleep(3)

    # pytest -s -v --headed .\test_54shadow_dom.py --slowmo=100