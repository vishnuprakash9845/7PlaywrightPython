from playwright.sync_api import Page, sync_playwright, expect
import time

def test_select_element_after_hover(page: Page) -> None:
    page.goto("https://www.globalsqa.com/demo-site/")
    time.sleep(1)

    free_book = page.locator("#menu-item-7128",has_text="Free Ebooks")
    free_book.hover()
    page.wait_for_timeout(3000)
    all_free_books = page.locator("//li[@id='menu-item-7128']//ul[@class='sub-menu']//a")
    print(all_free_books.all_inner_texts())

    free_deep_learning_book = page.locator(get_header_submenu("Free Ebooks","Free Tensorflow eBooks"))
    free_deep_learning_book.click()
    time.sleep(5)
    print(page.title())

    time.sleep(3)

def get_header_submenu(menu,submenu):
    return f"//div[@class='dark_menu']//a[.='{menu}']/parent::li//ul[@class='sub-menu']//a[contains(.,'{submenu}')]"

