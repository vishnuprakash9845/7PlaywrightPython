from playwright.sync_api import Playwright, sync_playwright, expect
import os


def run(playwright: Playwright) -> None:
    app_data_path = os.getenv("LOCALAPPDATA")
    user_data_path = os.path.join(app_data_path,'Chromium\\User Data\\Default')
    context = playwright.chromium.launch_persistent_context(user_data_path, channel='chrome', headless=False)
    #page = context.new_page()
    page = context.pages[0]
    page.goto("https://www.google.com/intl/en_in/gmail/about/")
    page.wait_for_timeout(5000)

    # ---------------------
    context.close()


with sync_playwright() as playwright:
    run(playwright)

#python test_66open_browser_incognito.py