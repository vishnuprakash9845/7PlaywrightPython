from playwright.sync_api import Page, sync_playwright, expect
import time

def test_click_for_js_alert(page: Page) -> None:
    page.goto("https://nxtgenaiacademy.com/alertandpopup/")
    #page.wait_for_timeout(2000)
    page.on("dialog", lambda dialog: print(dialog.message))
    click_js_alert_btn = page.locator("button[name='alertbox']")
    page.on("dialog", lambda dialog: dialog.accept()) 
    click_js_alert_btn.click()
    #page.wait_for_timeout(3000)

    time.sleep(1)

def test_click_for_js_confirm(page: Page) -> None:
    page.goto("https://nxtgenaiacademy.com/alertandpopup/")
    #page.wait_for_timeout(2000)
    page.on("dialog", lambda dialog: print(dialog.message))
    click_js_alert_btn = page.locator("button[name='confirmalertbox']")
    page.on("dialog", lambda dialog: dialog.accept("Playwright POC")) 
    click_js_alert_btn.click()
    #page.wait_for_timeout(3000)

    time.sleep(1)

def test_click_for_js_prompt_alert(page: Page) -> None:
    page.goto("https://nxtgenaiacademy.com/alertandpopup/")
    #page.wait_for_timeout(2000)
    page.on("dialog", lambda dialog: print(dialog.message))
    click_js_alert_btn = page.locator("button[name='promptalertbox1234']")
    page.on("dialog", lambda dialog: dialog.accept(prompt_text="Yes")) 
    click_js_alert_btn.click()
    #page.wait_for_timeout(3000)

    time.sleep(10)