
from POM.add_to_cart_page import CartPage
import time

def test_add_single_product(go_to_homepage):
    cart = CartPage(go_to_homepage.driver)  # inherits Homepage_class & ProductPage_class

    # Click first product
    cart.click_product()  # ProductPage_class
    cart.click_add_to_cart()  # ProductPage_class 
    cart.wait_for_alert().accept()  # Utils

    # Open cart and take screenshot
    cart.open_cart()  # AddToCartPage_class
    time.sleep(5)
    cart.screenshot("single_product_cart.png")  # Utils

def test_add_multiple_products(go_to_homepage):
    cart = CartPage(go_to_homepage.driver)

    products = ["Samsung galaxy s6", "Nokia lumia 1520"]
    for product in products:
        cart.click_product(product)  # ProductPage_class
        cart.click_add_to_cart()  # ProductPage_class 
        cart.wait_for_alert().accept()  # Utils

    cart.open_cart()  # AddToCartPage_class
    time.sleep(5)
    cart.screenshot("multiple_products_cart.png")  # Utils

    total = cart.get_total()  # AddToCartPage_class 
    print("Cart total:", total)

def test_delete_products(go_to_homepage):
    cart = CartPage(go_to_homepage.driver)

    # Add products
    products = ["Samsung galaxy s6", "Nokia lumia 1520"]
    for product in products:
        cart.click_product(product)
        cart.click_add_to_cart()
        cart.wait_for_alert().accept()

    cart.open_cart()
    cart.delete_first_product()  # AddToCartPage_class
    time.sleep(5)
    cart.screenshot("cart_after_deletion.png") 
