from playwright.sync_api import Page, sync_playwright, expect
import time

def test_click_for_js_alert(page: Page) -> None:
    page.goto("https://sweetalert2.github.io/")
    #page.wait_for_timeout(2000)

    show_success_msg = page.locator("div.showcase  button.show-example-btn")
    show_success_msg.click()
    #page.wait_for_timeout(3000)

    alert_msg = page.locator("#swal2-title")
    alert_msg_text = alert_msg.inner_text()
    print(alert_msg_text)
    assert alert_msg_text == 'Good job!'

    #ok_button = page.locator("//button[.='OK']")
    ok_button = page.locator("button",has_text='OK')
    ok_button.click()

    time.sleep(1)

    assert not alert_msg.is_visible(),"The sweet alert pop up does not get closed"

    time.sleep(1)