from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=1000)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://www.google.com/")
    print(page.url)

    page.locator("text=Gmail").click()
    print(page.url)

    page.go_back()
    print(page.url)

    page.go_forward()
    print(page.url)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
