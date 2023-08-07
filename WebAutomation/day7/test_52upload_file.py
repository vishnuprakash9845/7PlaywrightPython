from playwright.sync_api import Page, sync_playwright, expect
import time
import os

def test_upload_file(page: Page) -> None:
    page.goto("https://davidwalsh.name/demo/multiple-file-upload.php")

    #current_working_directory = os.getcwd()
    #os.path.join(current_working_directory,'testdata\\MyTestupload1.txt')
    print(os.getcwd())

    file_path1 = "C:\\Users\\invim19\\OneDrive - ABB\\Documents\\Others\\R\\Newfolder\\1.txt"
    file_path2 = "C:\\Users\\invim19\\OneDrive - ABB\\Documents\\Others\\R\\Newfolder\\2.txt"
    #page.set_input_files('input#filesToUpload',file_path)
    page.locator('input#filesToUpload').set_input_files([file_path1,file_path2])

    time.sleep(3)

    # pytest -s -v --headed .\test_52upload_file.py --slowmo=100