import pytest

@pytest.fixture()
def set_up_tear_down(page) -> None:
    page.set_viewport_size({"width":1536, "height": 722})
    page.goto("https://www.saucedemo.com/")
    yield page