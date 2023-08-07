from pom_framework.pages.ProductListPage import ProductListPage

class LoginPage:

    def __init__(self,page):
        self.page = page
        self._username = page.locator("#user-name")
        self._password = page.locator("#password")
        self._login_btn = page.locator("#login-button")

    def enter_username(self,username):
        self._username.clear()
        self._username.fill(username)

    def enter_password(self,password):
        self._password.clear()
        self._password.fill(password)

    def click_login(self):
        self._login_btn.click()

    def do_login(self, credentials):
        self.enter_username(credentials['username'])
        self.enter_password(credentials['password'])
        self.click_login()
        return ProductListPage(self.page)