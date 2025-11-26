import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BrowserUtils:

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title
    
    def wait_for_element(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))
    
    def take_screenshot(self, filename=None):
        if filename is None:
            filename = f"screenshot_{int(time.time())}.png"
        
        self.driver.save_screenshot(filename)
        print(f"Screenshot saved as {filename}")
        return filename

    def button_clicking(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def is_clickable(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            return True
        except:
            return False
