import pytest
from pages.order_page import OrderPage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestOrder:

    def test_order(self):
        login_page = LoginPage(self.driver)
        login_page.open_page()
        login_page.log_in()

        order_page = OrderPage(self.driver)
        order_page.addProductToBasket()
        order_page.checkOrder()
        order_page.fillOrder()
        order_page.checkOrder2()
        order_page.finish()
