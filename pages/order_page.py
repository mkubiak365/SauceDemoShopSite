import time
from allure_commons.types import AttachmentType
from locators import order_locators
import allure

class OrderPage:

    def __init__(self, driver):
        self.driver = driver
        self.add_product = order_locators.OrderLocators.add_product
        self.remove_product_element = order_locators.OrderLocators.remove_product_element
        self.shopping_card = order_locators.OrderLocators.shopping_card
        self.title = order_locators.OrderLocators.title
        self.description = order_locators.OrderLocators.description
        self.price = order_locators.OrderLocators.price
        self.checkout = order_locators.OrderLocators.checkout
        self.first_name = order_locators.OrderLocators.first_name
        self.last_name = order_locators.OrderLocators.last_name
        self.postal_code = order_locators.OrderLocators.postal_code
        self.continue_button = order_locators.OrderLocators.continue_button
        self.order_number = order_locators.OrderLocators.order_number
        self.order_delivery = order_locators.OrderLocators.order_delivery
        self.order_price = order_locators.OrderLocators.order_price
        self.finish_order = order_locators.OrderLocators.finish_order
        self.order_info = order_locators.OrderLocators.order_info

    @allure.step("Add product to basket.")
    def addProductToBasket(self):
        self.driver.find_element(*self.add_product).click()
        self.driver.find_element(*self.remove_product_element).is_displayed()

        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name="addProduct", attachment_type = AttachmentType.PNG)

        self.driver.find_element(*self.shopping_card).click()


    @allure.step("Check your basket.")
    def checkOrder(self):
        title = self.driver.find_element(*self.title).text
        assert title == order_locators.OrderInfo.title, 'No title'
        description = self.driver.find_element(*self.description).text
        assert description == order_locators.OrderInfo.description, 'No description'
        price = self.driver.find_element(*self.price).text
        assert price == order_locators.OrderInfo.price, 'No price'

        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name="basket", attachment_type=AttachmentType.PNG)

        self.driver.find_element(*self.checkout).click()


    @allure.step("Fill your order.")
    def fillOrder(self):
        self.driver.find_element(*self.first_name).send_keys("Adam")
        self.driver.find_element(*self.last_name).send_keys("Nowak")
        self.driver.find_element(*self.postal_code).send_keys("111-222")

        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name="order", attachment_type = AttachmentType.PNG)

        self.driver.find_element(*self.continue_button).click()


    @allure.step("Check order information.")
    def checkOrder2(self):
        self.driver.find_element(*self.order_number).is_displayed()
        self.driver.find_element(*self.order_delivery).is_displayed()
        self.driver.find_element(*self.order_price).is_displayed()
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name="orderData", attachment_type = AttachmentType.PNG)

    @allure.step("Finish your order.")
    def finish(self):
        self.driver.find_element(*self.finish_order).click()
        order_info = self.driver.find_element(*self.order_info).text
        assert order_info == order_locators.OrderInfo.order_thx_finish
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name="lastOrder", attachment_type = AttachmentType.PNG)

