from playwright.sync_api import Page, sync_playwright, expect
import time

def test_verify_css_properties(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    login_btn = page.get_by_text("Login")
    page.wait_for_timeout(2000)
    expect(login_btn).to_have_css("color","rgb(19, 35, 34)")
    expect(login_btn).to_have_css("text-align","center")
    expect(login_btn).to_have_css("font-style","normal")
    expect(login_btn).to_have_css("font-size","16px")

    # http://web.simmons.edu/~grabiner/comm244/weekthree/css-basic-properties.html
    # pytest -s -v --headed .\test_64verify_css_properties.py --slowmo=1000 --html=myreport.html --capture=tee-sys
    # pytest -s -v --headed .\test_64verify_css_properties.py