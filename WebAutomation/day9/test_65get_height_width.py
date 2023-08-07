from playwright.sync_api import Page, sync_playwright, expect
import time

def test_get_height_width(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    login_btn = page.get_by_text("Login")
    page.wait_for_timeout(2000)
    box = login_btn.bounding_box()
    height = box['height']
    width = box['width']

    print(f"Height of Login button is {height}")
    print(f"Width of Login button is {width}")

    # pytest -s -v --headed .\test_65get_height_width.py --slowmo=1000 --html=myreport.html --capture=tee-sys
    # pytest -s -v --headed .\test_65get_height_width.py