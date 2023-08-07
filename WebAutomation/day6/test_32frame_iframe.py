from playwright.sync_api import Page, sync_playwright, expect
import time

def test_autosuggestion(page: Page) -> None:
    page.goto("https://www.rediff.com/")
    page.wait_for_timeout(5000)

    #iframe_locator = page.frame("moneyiframe")
    #iframe_locator = page.main_frame.child_frames[0]
    mf = page.main_frame
    iframe_locator = get_frame_by_index(mf,0)
    print(type(iframe_locator))
    
    nse_index = iframe_locator.locator("span#nseindex")
    print(nse_index.inner_text())

    for iframe in page.main_frame.child_frames:
        print(iframe.name)

    print(len(page.main_frame.child_frames))

    page.wait_for_timeout(2000)

def get_frame_by_index(parent_frame,index):
    return parent_frame.child_frames[index]





