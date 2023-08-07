from playwright.sync_api import Page, expect
import time

def clear_inputtext(page, loc):
    page.locator(loc).press("Control+KeyA")
    page.locator(loc).press("Backspace")

def test_example(page: Page) -> None:

    page.goto("http://uitestingplayground.com/sampleapp")
    print(page.url)

    page.locator("input[name='UserName']").fill("username1")
    
    #page.locator("input[name='UserName']").fill("")
    clear_inputtext(page,"input[name='UserName']")

    #page.locator("input[name='UserName']").fill("prakash")
    page.locator("input[name='UserName']").type("prakash",delay=500)
    page.locator("input[name='Password']").fill("pwd")
    page.locator("#login").click()
    time.sleep(2)