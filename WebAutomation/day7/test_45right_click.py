from playwright.sync_api import Page, sync_playwright, expect
import time

def test_wait_till_loader_disappers(page: Page) -> None:
    page.goto("https://www.jqueryscript.net/demo/Tiny-jQuery-Plugin-For-Chrome-Style-Context-Menus-chromeContext/demo/")
    page.wait_for_timeout(3000)

    context_area = page.locator("div#one")
    context_area.click(button="right")

    time.sleep(1)


    # > pytest -s -v --headed .\test_45right_click.py   