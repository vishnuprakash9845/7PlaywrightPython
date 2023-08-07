from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=1000)
    context = browser.new_context()

    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto("https://www.google.com/")

    page.locator("[aria-label=\"Search\"]").click()

    page.locator("[aria-label=\"Search\"]").fill("Playwright")

    with page.expect_navigation():
        page.locator("[aria-label=\"Search\"]").press("Enter")

    page.locator("text=Playwright: Fast and reliable end-to-end testing for modern ...").click()

    # Stop tracing and export it into a zip archive.
    context.tracing.stop(path = "trace.zip")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
