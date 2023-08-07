from playwright.sync_api import Page, sync_playwright, expect
import time

def test_handle_graphs(page: Page) -> None:
    # page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    # page.locator("//button[@class='btn btn-primary btn-lg' and contains(.,'Customer')]").click()
    # page.locator("#userSelect").select_option(index=2)
    # page.locator("#userSelect").select_option(value="4")
    # page.locator("//button[@class='btn btn-default' and contains(.,'Login')]").click()
    # #page.wait_for_timeout(3000)
    # page.wait_for_timeout(2000)

    with page.expect_request("**/account") as req:
        page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
        page.locator("//button[@class='btn btn-primary btn-lg' and contains(.,'Customer')]").click()
        page.locator("#userSelect").select_option(index=2)
        page.locator("//button[@class='btn btn-default' and contains(.,'Login')]").click()

    print(req.value.url)
    print(req.value.method)
    print(req.value.redirected_from)
    print(req.value.resource_type)
    print(req.value.redirected_to)
    print(req.value.all_headers())


    
    # pytest -s -v --headed .\test_63inspect_network_traffic.py --slowmo=1000 --html=myreport.html --capture=tee-sys
    # pytest -s -v --headed .\test_63inspect_network_traffic.py