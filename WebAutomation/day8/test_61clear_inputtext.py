from playwright.sync_api import Page, sync_playwright, expect
import time

def test_cleat_input_textfield(page: Page) -> None:
    page.goto("https://www.google.com/")
    search_input = page.get_by_title("Search")
    search_input.fill("Playwright")

    search_input.clear(force=True)

    page.wait_for_timeout(2000)
    expect(search_input).to_be_empty()

    
    # pytest -s -v --headed .\test_61clear_inputtext.py --slowmo=1000 --html=myreport.html --capture=tee-sys
    # pytest -s -v --headed .\test_61clear_inputtext.py