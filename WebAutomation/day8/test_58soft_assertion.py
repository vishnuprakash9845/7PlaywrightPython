from playwright.sync_api import Page, sync_playwright, expect
import time
from pytest_check import check

def test_soft_assertion(page: Page) -> None:
    page.goto("https://jqueryui.com/tooltip/")
    age = page.frame_locator("//iframe").locator("#age")
    age.hover()

    tool_tip_msg = page.frame_locator("//iframe").locator("div.ui-tooltip-content")
    print(tool_tip_msg.inner_text())

    # Hard Assertions
    # expected_txt = "We ask for your age only for statistical purposes.."
    # expect(tool_tip_msg).to_have_text(expected_txt)
    # expect(age).to_be_empty()
    #age.fill("25")
    #expect(age).not_to_be_empty()
    #expect(age).to_have_value("25")

    # Soft Assertions (install pytest_check)
    expected_txt = "We ask for your age only for statistical purposes."
    check.equal(tool_tip_msg.inner_text(),expected_txt)
    value1 = age.input_value()
    check.equal(value1,"")
    age.fill("25")
    value2 = age.input_value()
    check.equal(value2,"25")

    # pytest -s -v --headed .\test_58soft_assertion.py --slowmo=1000 --html=myreport.html --capture=tee-sys