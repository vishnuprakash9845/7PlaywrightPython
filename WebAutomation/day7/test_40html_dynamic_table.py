from playwright.sync_api import Page, sync_playwright, expect
import time

def test_angular_web_table(page: Page) -> None:
    page.goto("https://www.w3schools.com/html/html_tables.asp")
    
    rows = page.locator("table#customers tr")
    index=0
    while index < rows.count():
        print(rows.nth(index).inner_text())
        index+=1

    company_name = "Ernst Handel"
    column_name = "Contact"
    contact_value = get_data_by_company(page, company_name, column_name)
    print(contact_value)
    time.sleep(1)
    column_data = get_all_data_for_a_column(page, column_name)
    print(column_data)
    time.sleep(1)

def get_data_by_company(page, company_name, column_name):
    rows = page.locator("table#customers tr")  
    column_headers = page.locator("table#customers th")
    column_index = None
    index=1
    while index <= column_headers.count():
       if column_headers.nth(index-1).inner_text() == column_name:
          column_index = index
       index +=1

   
    contact = rows.locator(":scope", has_text=company_name).locator(f"//td[{column_index}]")
    print(contact.inner_text())
    return contact.inner_text()

def get_all_data_for_a_column(page, column_name):
    column_index = None
    column_headers = page.locator("table#customers th")
    column_index = None
    index=1
    while index <= column_headers.count():
       if column_headers.nth(index-1).inner_text() == column_name:
          column_index = index
       index +=1

    column_data = page.locator(f"//table[@id='customers']//tr/td[{column_index}]")
    return column_data.all_inner_texts()
