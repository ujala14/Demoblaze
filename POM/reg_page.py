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
        self.button_clicking(self.nav_Sign_up_button)
    
    def get_modal_heading(self):
        return self.get_text(self.modal_heading)
        
    def field_visible(self):
        return self.is_visible(self.field_username) and self.is_visible(self.field_password)

    def fileds_clickable(self):
        return self.is_clickable(self.field_username) and self.is_clickable(self.field_password)
  
    def valid_reg_credentials_enter(self, username):
        self.driver.find_element(self.field_username).send_keys(username)
    
       
        


    
