from playwright.sync_api import Page, sync_playwright, expect
import time

def test_autosuggestion(page: Page) -> None:
    page.goto("https://jqueryui.com/autocomplete/")
    #page.wait_for_timeout(5000)

    frame_element = page.frame_locator("iframe.demo-frame")
    input_field = frame_element.locator("input.ui-autocomplete-input")
    input_field.fill("wa")
    page.wait_for_timeout(3000)

    #time.sleep(3)

def test_iframe2_ByID(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com.iframe")
    #page.wait_for_timeout(5000)

    input_area = page.frame("mce_0_ifr").locator("body#tinymce")
    input_area.type("AutomationNeema")
    page.wait_for_timeout(3000)


