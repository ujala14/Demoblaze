from selenium.webdriver.common.by import By
from Utils.browsersutils import BrowserUtils

class login_modal_class(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.nav_login_button = (By.LINK_TEXT, "Sign up")
        self.modal_heading = (By.XPATH, "//*[@id='signInModalLabel']")
        self.field_username = (By.ID, "sign-username")
        self.field_password = (By.ID, "sign-password")
        self.login_close_button = (By.XPATH, "//*[@id='signInModal']/div/div/div[3]/button[1]")
        self.login_button = (By.CSS_SELECTOR, "button.btn-primary[onclick='register()']")
        #self.logout_button = 

    #UI test cases of login page
    def login_modal(self):
        self.button_clicking(self.nav_login_button)
    
    def get__login_modal_heading(self):
        return self.get_text(self.modal_heading)
        
    def login_field_visible(self):
        return self.is_visible(self.field_username) and self.is_visible(self.field_password)

    def login_fileds_clickable(self):
        return self.is_clickable(self.field_username) and self.is_clickable(self.field_password)
  
  
  #functional test cases of login page
    def valid_login__username(self, username):
        self.clear_field(self.field_username)
        self.send_keys(self.field_username,username)

    def valid_login_password(self, password):
        self.clear_field(self.field_password)
        self.send_keys(self.field_password,password)

    def form_reset_validation(self):
        return self.driver.find_element(*self.field_username).get_attribute("value") and self.driver.find_element(*self.field_password).get_attribute("value")
       
    def password_masking_check(self):
        return self.driver.find_element(*self.field_password).get_attribute("type") == "pssword"
       
       
        
       
        


    
