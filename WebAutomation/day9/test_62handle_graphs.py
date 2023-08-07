from playwright.sync_api import Page, sync_playwright, expect
import time

def test_handle_graphs(page: Page) -> None:
    page.goto("https://frappe.io/charts")
    events_list = page.locator("//figure[@id='line-composite-1']//*[name()='svg']//*[local-name()='circle']/following-sibling::*[local-name()='text']")
    print(events_list.count())
    index=0
    while index<events_list.count():
        print(events_list.nth(index).text_content())
        index+=1
    page.wait_for_timeout(2000)

    
    # pytest -s -v --headed .\test_62handle_graphs.py --slowmo=1000 --html=myreport.html --capture=tee-sys
    # pytest -s -v --headed .\test_62handle_graphs.py