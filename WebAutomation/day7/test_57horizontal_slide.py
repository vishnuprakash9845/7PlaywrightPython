from playwright.sync_api import Page, sync_playwright, expect
import time
import os

def test_horizontal_slide(page: Page) -> None:
    page.goto('https://codepen.io/BoringCode/pen/nYbrep')

    send_btn = page.frame_locator("#result").locator("//button[.='Send >>']")
    slide_to_send = page.frame_locator("#result").locator("div.slide-submit>label")
    send_btn.click()
    page.wait_for_timeout(2000)
    send_btn.drag_to(slide_to_send)
    # time.sleep(3)
    page.wait_for_timeout(5000)

    # pytest -s -v --headed .\test_57horizontal_slide.py --slowmo=100