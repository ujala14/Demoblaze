from selenium.webdriver.common.by import By
from Utils.browsersutils import BrowserUtils
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class reg_modal_class(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.nav_Sign_up_button = (By.LINK_TEXT, "Sign up")
        self.modal_heading = (By.XPATH, "//*[@id='signInModalLabel']")
        self.field_username = (By.ID, "sign-username")
        self.field_password = (By.ID, "sign-password")
        self.signup_close_button = (By.XPATH, "//*[@id='signInModal']/div/div/div[3]/button[1]")
        self.signup_register_button = (By.CSS_SELECTOR, "button.btn-primary[onclick='register()']")

    def sign_up_modal(self):
        self.driver.find_element(*self.nav_Sign_up_button).click()
        
    
    def get_modal_heading(self):
        heading_ele = self.wait_for_element(self.modal_heading, timeout=10)
        return heading_ele.text
        
    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
    
    
    def is_clickable(self, locator):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
            return True
        except:
            return False
    
       
        


    
