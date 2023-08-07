from playwright.sync_api import Page, sync_playwright, expect
import time
import os

def test_download_file(page: Page) -> None:
    page.goto("https://demo.automationtesting.in/FileDownload.html")

    with page.expect_download() as download_i:
        #page.locator("//a[text()='selenium.txt']").click()
        page.locator("a.btn").click()
    dl = download_i.value
    print(dl.path())
    working_dir_path = os.getcwd()
    final_path = os.path.join(working_dir_path,"testdata/myfile.pdf")
    dl.save_as(final_path)

    time.sleep(3)

    # pytest -s -v --headed .\test_53download_file.py --slowmo=100