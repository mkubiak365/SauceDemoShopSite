import time
from allure_commons.types import AttachmentType
from locators import product_locators
import allure

class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.add_button = product_locators.ProductLocators.add_button
        self.title = product_locators.ProductLocators.title
        self.description = product_locators.ProductLocators.description
        self.price = product_locators.ProductLocators.price

    @allure.step("Check title, description and price.")
    def checkProductSite(self):
        self.driver.find_element(*self.add_button).click()
        title = self.driver.find_element(*self.title).text
        descritpion = self.driver.find_element(*self.description).text
        price = self.driver.find_element(*self.price).text

        assert title == "Sauce Labs Bike Light", 'No title'
        assert descritpion == "A red light isn't the desired state in testing but it sure helps when riding your bike at night. Water-resistant with 3 lighting modes, 1 AAA battery included.", 'No description'
        assert price == "$9.99", 'No price'
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name="product", attachment_type = AttachmentType.PNG)

