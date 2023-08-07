from playwright.sync_api import Page, sync_playwright, expect
import time

def test_get_text(page: Page) -> None:
    page.goto("https://www.spicejet.com/")
    time.sleep(1)
    from_input=page.locator("//div[.='From']/div/input")
    from_input.click()
    from_input.fill("Ko")
    page.locator(get_loc_city("CCU")).click()
    time.sleep(5)

def get_loc_city(city):
    return f"(//div[.='{city}'])[2]"