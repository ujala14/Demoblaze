from selenium.webdriver.common.by import By
from Utils.browsersutils import BrowserUtils

class Homepage_class(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)

    # ===== NAVBAR =====
        self.NAV_BRAND = (By.ID, "nava")
        self.NAV_HOME = (By.CSS_SELECTOR, "a.nav-link[href='index.html']")
        self.NAV_CONTACT = (By.LINK_TEXT, "Contact")
        self.NAV_ABOUT = (By.LINK_TEXT, "About us")
        self.NAV_CART = (By.ID, "cartur")
        self.NAV_LOGIN = (By.ID, "login2")
        self.NAV_SIGNUP = (By.ID, "signin2")

    # ===== CATEGORIES =====
        self.CAT_PHONES = (By.LINK_TEXT, "Phones")
        self.CAT_LAPTOPS = (By.LINK_TEXT, "Laptops")
        self.CAT_MONITORS = (By.LINK_TEXT, "Monitors")

    # ===== PRODUCT GRID =====
        self.PRODUCT_CARD = (By.CLASS_NAME, "card")
        self.PRODUCT_IMAGE = (By.CLASS_NAME, "card-img-top")
        self.PRODUCT_TITLE = (By.CLASS_NAME, "card-title")
        self.PRODUCT_PRICE = (By.TAG_NAME, "h5")

    # ===== PAGINATION =====
        self.NEXT_BUTTON = (By.ID, "next2")
        self.PREV_BUTTON = (By.ID, "prev2")

    # ===== FOOTER =====
        self.FOOTER = (By.ID, "footc")

    # ===== NAVBAR METHODS =====
    def navbar_items_status(self):
        return {
            "brand": self.is_visible(self.NAV_BRAND),
            "Home": self.is_visible(self.NAV_HOME),
            "contact": self.is_visible(self.NAV_CONTACT),
            "about_us": self.is_visible(self.NAV_ABOUT),
            "cart": self.is_visible(self.NAV_CART),
            "login": self.is_visible(self.NAV_LOGIN),
            "signup": self.is_visible(self.NAV_SIGNUP)
        }

    # ===== CATEGORIES METHODS =====
    def get_categories_present(self):
        return {
            "phones": self.is_visible(self.CAT_PHONES),
            "laptops": self.is_visible(self.CAT_LAPTOPS),
            "monitors": self.is_visible(self.CAT_MONITORS)
        }

    # ===== PRODUCT GRID METHODS =====
    def get_product_cards(self):
        return self.driver.find_elements(*self.PRODUCT_CARD)

    def get_product_titles(self):
        cards = self.get_product_cards()
        return [card.find_element(*self.PRODUCT_TITLE).text for card in cards]

    def get_product_images(self):
        cards = self.get_product_cards()
        return [card.find_element(*self.PRODUCT_IMAGE).get_attribute("src") for card in cards]

    def get_product_prices(self):
        cards = self.get_product_cards()
        return [card.find_element(*self.PRODUCT_PRICE).text for card in cards]

    # ===== PAGINATION METHODS =====
    def click_next_button(self):
        self.button_clicking(self.NEXT_BUTTON)

    def click_prev_button(self):
        self.button_clicking(self.PREV_BUTTON)

    def is_next_clickable(self):
        return self.is_clickable(self.NEXT_BUTTON)

    def is_prev_clickable(self):
        return self.is_clickable(self.PREV_BUTTON)

    # ===== FOOTER =====
    def is_footer_visible(self):
        return self.is_visible(self.FOOTER)
