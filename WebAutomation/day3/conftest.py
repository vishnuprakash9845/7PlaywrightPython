from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

@pytest.fixture(scope="function")
def set_up(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    yield page
    context.close()
    browser.close()

@pytest.fixture(scope="function")
def set_up_tear_down(page) -> None:
    page.set_viewport_size({"width":1536, "height": 722})
    page.goto("https://www.saucedemo.com/")
    yield page