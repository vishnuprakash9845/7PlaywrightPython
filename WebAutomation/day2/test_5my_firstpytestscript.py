from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.get_by_text("Accepted usernames are:standard_userlocked_out_userproblem_userperformance_glitc").dblclick()
    page.get_by_text("Accepted usernames are:standard_userlocked_out_userproblem_userperformance_glitc").dblclick()
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"password\"]").press("Enter")
    page.get_by_role("button", name="Open Menu").click()
    page.get_by_role("link", name="Logout").click()

    print("test Completed")