from selenium.webdriver.common.by import By
from Utils.browsersutils import BrowserUtils

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
  
  
  #functional test cases of registeration/signup page
    def valid_username(self, username):
        self.clear_field(self.field_username)
        self.send_keys(self.field_username,username)

    def valid_password(self, password):
        self.clear_field(self.field_password)
        self.send_keys(self.field_password,password)

    def form_reset_validation(self):
        username_value = (driver).find_element(*self.field_username).get_attribute("value")
        password_value = (driver).find_element(*self.field_password).get_attribute("value")
        return {"username": username_value, "password": password_value}

    def password_masking_check(self):
        return (driver).find_element(*self.field_password).get_attribute("type") == "password"
       
        


    
