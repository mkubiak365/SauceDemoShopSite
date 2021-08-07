from allure_commons.types import AttachmentType
import time

from locators import home_locators
import allure

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.product = home_locators.HomePageLocators.product
        self.price = home_locators.HomePageLocators.price
        self.product2 = []
        self.price2 = []
        self.validateList = []



    def getProduct(self):
        for a in self.driver.find_elements(*self.product):
            self.product2.append(a.text)

    def getPrice(self):
        for b in self.driver.find_elements(*self.price):
            self.price2.append(b.text)

    @allure.step("Check the product titles and prices.")
    def validateProductAndPrice(self):
        for c in range(0, 6):
            self.validateList.append(self.product2[c] + " " + self.price2[c])


        assert self.validateList == home_locators.HomePageList.assert_list, 'No validate'
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name="productsInCategory", attachment_type = AttachmentType.PNG)





