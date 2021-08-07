import pytest
from pages.login_page import LoginPage



@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.open_page()
        login_page.log_in()