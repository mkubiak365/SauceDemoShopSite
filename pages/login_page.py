import time
from allure_commons.types import AttachmentType
from locators import login_locators
import allure

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.login = login_locators.LoginLocators.login
        self.password = login_locators.LoginLocators.password
        self.login_button = login_locators.LoginLocators.login_button
        self.validate_login = login_locators.LoginLocators.validate_login

    @allure.step("Login to the site.")
    def log_in(self):
        self.driver.find_element(*self.login).send_keys("standard_user")
        self.driver.find_element(*self.password).send_keys("secret_sauce")
        self.driver.find_element(*self.login_button).click()
        self.driver.find_element(*self.validate_login).is_displayed()
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name="login", attachment_type = AttachmentType.PNG)


    def open_page(self):
        self.driver.get("https://www.saucedemo.com/")

