from playwright.sync_api import Page, sync_playwright, expect
import time

def test_toast_message(page: Page) -> None:
    page.goto("https://codeseven.github.io/toastr/demo.html")
    
    show_toast_btn = page.locator("button#showtoast")
    show_toast_btn.click()
    toast_message = page.locator("div.toast-message")
    print(toast_message.inner_text())


    # pytest -s -v --headed .\test_51toast_message.py --slowmo=100