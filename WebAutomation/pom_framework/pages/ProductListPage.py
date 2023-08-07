
class ProductListPage:

    def __init__(self,page):
        self.page=page
        self._productlist_header = page.locator("span.title")

    @property
    def product_header(self):
        return self._productlist_header
