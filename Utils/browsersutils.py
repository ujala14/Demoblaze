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