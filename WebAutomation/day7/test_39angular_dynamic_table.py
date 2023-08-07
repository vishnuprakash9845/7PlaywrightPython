from playwright.sync_api import Page, sync_playwright, expect
import time

def test_angular_web_table(page: Page) -> None:
    page.goto("https://primeng.org/table")
    print(page.title())
    time.sleep(1)
    page.locator("//button[.='Row Selection']").click()
    time.sleep(1)
    page.locator("//button[contains(.,'Checkbox Selection')]").click()
    time.sleep(2)
    
    #method-1
    rows = page.locator("//h3[contains(.,'Checkbox Selection ')]/../following-sibling::div//table//tr")
    print(rows)
    print(rows.count())
    checkbox = rows.locator(":scope", has_text="nvklal433").locator("div.p-checkbox-box")
    print(checkbox)
    print(checkbox.count())
    checkbox.check()

    expect(checkbox).to_be_checked()

    #method-2
    # index=0
    # while index < rows.count():
    #     print(rows.nth(index).inner_text())
    #     index+=1

    # checkbox = page.locator("//h3[contains(.,'Checkbox Selection ')]/../following-sibling::div//table//td[.='Bamboo Watch']/..//div[@role='checkbox']")
    # print(checkbox)
    # print(checkbox.count())
    # checkbox.check()

    expect(checkbox).to_be_checked()
    time.sleep(5)