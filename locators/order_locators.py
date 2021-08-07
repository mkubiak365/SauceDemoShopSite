from selenium.webdriver.common.by import By

class OrderLocators:

    add_product = (By.ID, "add-to-cart-sauce-labs-backpack")
    remove_product_element = (By.NAME, "remove-sauce-labs-backpack")
    shopping_card = (By.ID, "shopping_cart_container")
    title = (By.CLASS_NAME, "inventory_item_name")
    description = (By.CLASS_NAME, "inventory_item_desc")
    price = (By.CLASS_NAME, "inventory_item_price")
    checkout = (By.ID, "checkout")
    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    order_number = (By.XPATH, "//*[text()='SauceCard #31337']")
    order_delivery = (By.XPATH, "//*[text()='FREE PONY EXPRESS DELIVERY!']")
    order_price = (By.XPATH, "//*[text()='32.39']")
    finish_order = (By.ID, "finish")
    order_info = (By.CLASS_NAME, "complete-header")

class OrderInfo:

    title = "Sauce Labs Backpack"
    description = "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection."
    price = "$29.99"
    order_thx_finish = "THANK YOU FOR YOUR ORDER"

