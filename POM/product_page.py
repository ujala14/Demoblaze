from POM.home_page import Homepage_class
from selenium.webdriver.common.by import By

class ProductDetail_class(Homepage_class):
    def __init__(self, driver):
        super().__init__(driver)

        # Product detail page locators
        self.PRODUCT_NAME = (By.TAG_NAME, "h2")          # Product title on detail page
        self.PRODUCT_PRICE = (By.TAG_NAME, "h3")         # Price text (e.g., "$790")
        self.ADD_TO_CART = (By.LINK_TEXT, "Add to cart") # Add to cart button
        self.PRODUCT_IMAGE = (By.XPATH, "//*[@id='imgp']/div/img") # Product image

    # Click any product from product list (first product by default)
    def click_product(self, product_name=None):
        cards = self.get_product_cards()  # inherited from Homepage_class
        if product_name:
            for card in cards:
                title = card.find_element(*self.PRODUCT_TITLE).text
                if title == product_name:
                    card.click()
                    return
        else:
            cards[0].click()  # Click first product if no name given

    # Get product price text
    def get_product_price(self):
        return self.get_text(self.PRODUCT_PRICE)

    # Click Add to Cart button
    def click_add_to_cart(self):
        self.button_clicking(self.ADD_TO_CART)

    # Check if product image is visible
    def is_product_image_visible(self):
        return self.is_visible(self.PRODUCT_IMAGE)
    
     # Take screenshot
    def screenshot(self, filename):
        return self.take_screenshot(filename)
