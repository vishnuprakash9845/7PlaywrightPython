from playwright.sync_api import Page, sync_playwright, expect
import time

def test_wait_till_loader_disappers(page: Page) -> None:
    page.goto("https://www.flaticon.com/free-icons/loading?word=loading")
    #page.wait_for_timeout(3000)
    loading_icon = page.locator("div.container-filters div.circle-spinner")
    expect(loading_icon).not_to_be_visible(timeout=5000)

    colors_text = page.locator("//p[contains(.,'Colors')]")
    page.locator("//span[@class='item__link' and text()=' Black']").click()
    page.locator("//span[@class='item__link' and text()=' Outline']").click()
    page.locator("//span[@class='item__link' and text()='Recent']").click()

    time.sleep(1)


    # > pytest -s -v --headed .\test_44wait_till_loading.py