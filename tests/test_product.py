import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestProduct:

    def test_product(self):
        login_page = LoginPage(self.driver)
        login_page.open_page()
        login_page.log_in()

        product_page = ProductPage(self.driver)
        product_page.checkProductSite()