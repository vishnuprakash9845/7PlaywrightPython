from playwright.sync_api import Page, sync_playwright, expect
import time

def test_field_editable(page: Page) -> None:
    page.goto("https://jsfiddle.net/L96svw3c")
    editable_field = page.frame("result").locator("#readonly")
    expect(editable_field).to_be_editable()
    time.sleep(1)

def test_readonly_field(page: Page) -> None:
    page.goto("https://jsfiddle.net/L96svw3c")
    read_only_field = page.frame("result").locator("#readOnly")
    expect(read_only_field).not_to_be_editable()
    time.sleep(1)

#pytest -s -v --headed .\test_41verify_read_only.py