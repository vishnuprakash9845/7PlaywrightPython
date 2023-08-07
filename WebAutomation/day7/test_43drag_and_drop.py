from playwright.sync_api import Page, sync_playwright, expect
import time

def test_drag_and_drop1(page: Page) -> None:
    page.goto("https://ui.vision/demo/webtest/dragdrop/")
    page.wait_for_timeout(3000)
    src = page.locator("#one")
    dest = page.locator("div#bin")
    src.drag_to(dest)
    time.sleep(1)

def test_drag_and_drop2(page: Page) -> None:
    page.goto("https://demo.automationtesting.in/Static.html")
    page.wait_for_timeout(3000)
    page.drag_and_drop('#mongo','#droparea')
    time.sleep(1)

def test_drag_and_drop3(page: Page) -> None:
    page.goto("https://webflow.com/made-in-webflow/website/drag-drop-demo")
    page.wait_for_timeout(1000)
    src = page.frame_locator("//iframe").locator("#draggable")
    dest = page.frame_locator("//iframe").locator("#droppable.ui-widget-header")
    src.hover()
    page.mouse.down()
    dest.hover()
    page.mouse.up()

    # pytest -s -v --headed .\test_43drag_and_drop.py --slowmo=2000
    # pytest -s -v --headed .\test_43drag_and_drop.py::test_drag_and_drop3 --slowmo=2000