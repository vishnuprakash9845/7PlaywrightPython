from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

@pytest.mark.regression
@pytest.mark.parametrize("username, password", [("standard_user","secret_sauce"),
                                                ("",""),
                                              pytest.param("problem_user","secret_sauce",marks=pytest.mark.xfail),
                                              ("performance_glitch_user","secret_sauce")])
def test_login_with_ddt(set_up_tear_down,username, password) -> None:
    page = set_up_tear_down

    page.locator("#user-name").fill(username,timeout=3000)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()

    burger_menu = page.locator("#react-burger-menu-btn")
    burger_menu.click(timeout=3000)

# pytest -s -v --headed .\test_55attach_screenshot.py --slowmo=100 --html=myreport.html --capture=tee-sys