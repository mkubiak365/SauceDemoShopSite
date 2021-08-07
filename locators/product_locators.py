from selenium.webdriver.common.by import By

class ProductLocators:

    add_button = (By.XPATH, "//div[@class='inventory_item_name'][text()='Sauce Labs Bike Light']")
    title = (By.XPATH, "//div[@class='inventory_details_name large_size']")
    description = (By.XPATH, "//div[@class='inventory_details_desc large_size']")
    price = (By.XPATH, "//div[@class='inventory_details_price']")
