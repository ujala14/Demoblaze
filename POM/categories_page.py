from POM.home_page import Homepage_class
from selenium.webdriver.common.by import By

class Categories_class(Homepage_class):
    def __init__(self, driver):
        super().__init__(driver)

        # Category locators
        self.PHONES = (By.LINK_TEXT, "Phones")
        self.LAPTOPS = (By.LINK_TEXT, "Laptops")
        self.MONITORS = (By.LINK_TEXT, "Monitors")

    # Click any category dynamically using utils click method
    def click_category(self, category_name):
        category_name = category_name.lower()
        if category_name == "phones":
            self.button_clicking(self.PHONES)
        elif category_name == "laptops":
            self.button_clicking(self.LAPTOPS)
        elif category_name == "monitors":
            self.button_clicking(self.MONITORS)
        else:
            raise ValueError(f"Unknown category: {category_name}")

    # Take screenshot using utils method
    def screenshot_category(self, filename=None):
        return self.take_screenshot(filename)
