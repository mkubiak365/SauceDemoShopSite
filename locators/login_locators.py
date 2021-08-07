from selenium.webdriver.common.by import By

class LoginLocators:

    login = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")
    validate_login = (By.XPATH, "//*[text()='Logout']")
