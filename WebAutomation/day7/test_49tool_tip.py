from playwright.sync_api import Page, sync_playwright, expect
import time

def test_double_click(page: Page) -> None:
    page.goto("https://jqueryui.com/tooltip/")
    age = page.frame_locator("//iframe").locator("#age")
    age.hover()

    tool_tip_msg = page.frame_locator("//iframe").locator("div.ui-tooltip-content")
    print(tool_tip_msg.inner_text())

    expected_txt = "We ask for your age only for statistical purposes."
    expect(tool_tip_msg).to_have_text(expected_txt)

    # pytest -s -v --headed .\test_48tool_tip.py --slowmo=3000