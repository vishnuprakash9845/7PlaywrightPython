from playwright.sync_api import Page, sync_playwright, expect
import time

def test_horizontal_slider(page: Page) -> None:
    page.goto("https://www.globalsqa.com/demo-site/sliders/")
    
    green = page.frame_locator("//iframe[contains(@data-src,'colorpicker')]").locator("div#green span.ui-slider-handle")
    blue = page.frame_locator("//iframe[contains(@data-src,'colorpicker')]").locator("div#blue span.ui-slider-handle")
    range_max=25
    horizontalscroll(page,green,range_max)
    horizontalscroll(page,blue,range_max)

def horizontalscroll(page, locator, times):
    index=0
    while index <= times:
        locator.press('ArrowRight')
        print(index)
        index+=1

    # pytest -s -v --headed .\test_50horizontal_slider.py --slowmo=100