from selenium.webdriver.common.by import By
from POM.product_page import ProductDetail_class

class CartPage(ProductDetail_class):

    def __init__(self, driver):
        super().__init__(driver)

        self.CART_LINK = (By.ID, "cartur")
        self.PRODUCT_ROWS = (By.XPATH, "//tr[@class='success']")
        self.TOTAL_PRICE = (By.ID, "totalp")
        self.DELETE_LINK = (By.XPATH, "//a[text()='Delete']")

    # Go to Cart page
    def open_cart(self):
        self.button_clicking(self.CART_LINK)

    # Get all product row web elements
    def get_cart_items(self):
        return self.driver.find_elements(*self.PRODUCT_ROWS)

    # Get total price text
    def get_total(self):
        return self.get_text(self.TOTAL_PRICE)

    # Delete first product (Demoblaze deletes by row index)
    def delete_first_product(self):
        delete_buttons = self.driver.find_elements(*self.DELETE_LINK)
        if delete_buttons:
            delete_buttons[0].click()
