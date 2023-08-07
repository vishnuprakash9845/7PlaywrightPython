from playwright.sync_api import Page, sync_playwright, expect
import time

def test_new_locators(page: Page) -> None:
    page.goto("https://www.google.com/")
    search_input = page.get_by_title("Search")
    #search_input.fill("Playwright")

    page.keyboard.press('P')
    page.keyboard.press('l')
    page.keyboard.press('a')
    page.keyboard.press('y')

    page.wait_for_timeout(1000)

    search_input.blur()

    page.keyboard.press('w')
    page.keyboard.press('r')
    page.keyboard.press('i')
    page.keyboard.press('g')
    page.keyboard.press('h')
    page.keyboard.press('t')

    page.wait_for_timeout(1000)

    value = search_input.input_value()
    print(value)

    expect(search_input).to_have_value('Play')
    
    # pytest -s -v --headed .\test_60remove_focus.py --slowmo=1000 --html=myreport.html --capture=tee-sys
    # pytest -s -v --headed .\test_60remove_focus.py