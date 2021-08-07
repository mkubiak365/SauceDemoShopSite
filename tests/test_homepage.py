import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage


@pytest.mark.usefixtures("setup")
class TestHomePage:

    def test_homepage(self):
        login_page = LoginPage(self.driver)
        login_page.open_page()
        login_page.log_in()

        home_page = HomePage(self.driver)
        home_page.getProduct()
        home_page.getPrice()
        home_page.validateProductAndPrice()