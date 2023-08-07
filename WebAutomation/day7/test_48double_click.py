from playwright.sync_api import Page, sync_playwright, expect
import time

def test_double_click(page: Page) -> None:
    page.goto("https://api.jquery.com/dblclick/")
    page.wait_for_timeout(1000)
    color_box = page.frame_locator("//iframe").locator("//span[text()='Double click the block']/parent::body/div")
    page.wait_for_timeout(1000)
    color_box.dblclick()
    page.wait_for_timeout(1000)

    expect(color_box).to_have_class('dbl')

    # pytest -s -v --headed .\test_48double_click.py --slowmo=3000