from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/intl/en_in/gmail/about/")
    page.get_by_role("link", name="Sign in").click()
    page.get_by_role("heading", name="Sign in").click(button="right")

    signinTest1 = page.query_selector("text='Sign in'")
    print(signinTest1.inner_html())

    signinTest2 = page.query_selector("h1#headingText >> text=Sign in")
    print(signinTest2.inner_html())

    signinTest3 = page.query_selector("h1#headingText >> ..")
    print(signinTest3.inner_html())

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
