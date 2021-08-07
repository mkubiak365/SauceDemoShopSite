from selenium.webdriver.common.by import By

class HomePageLocators:

    product = (By.XPATH, "//div[@class='inventory_item_name']")
    price = (By.XPATH, "//div[@class='inventory_item_price']")

class HomePageList:
    assert_list = ["Sauce Labs Backpack $29.99", "Sauce Labs Bike Light $9.99", "Sauce Labs Bolt T-Shirt $15.99",
                   "Sauce Labs Fleece Jacket $49.99", "Sauce Labs Onesie $7.99",
                   "Test.allTheThings() T-Shirt (Red) $15.99"]



