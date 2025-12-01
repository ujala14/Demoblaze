from selenium.webdriver.common.by import By
from Utils.browsersutils import BrowserUtils

class login_modal_class(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.nav_login_button = (By.LINK_TEXT, "Log in")
        self.modal_heading = (By.XPATH, "//*[@id='logInModalLabel']")
        self.field_username = (By.ID, "loginusername")
        self.field_password = (By.ID, "loginpassword")
        self.login_close_button = (By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[1]")
        self.login_button = (By.CSS_SELECTOR, "button.btn-primary[onclick='logIn()']")
        self.logout_button = (By.LINK_TEXT, "Log out")
        self.welcome_msg = (By.ID, "nameofuser")

    #UI test cases of login page
    def login_modal(self):
        self.button_clicking(self.nav_login_button)
    
    def get_login_modal_heading(self):
        return self.get_text(self.modal_heading)
        
    def login_field_visible(self):
        return self.is_visible(self.field_username) and self.is_visible(self.field_password)

    def login_fileds_clickable(self):
        return self.is_clickable(self.field_username) and self.is_clickable(self.field_password)
  
  #functional test cases of login page
    def valid_login_username(self, username):
        self.clear_field(self.field_username)
        self.send_keys(self.field_username,username)

    def valid_login_password(self, password):
        self.clear_field(self.field_password)
        self.send_keys(self.field_password,password)
       
    def password_masking_check(self):
        return (driver).find_element(*self.field_password).get_attribute("type") == "password"

    def get_welcome_message(self):
        return self.get_text(self.welcome_msg)



        
       
        


    

