import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from POM.reg_page import reg_modal_class
from POM.login_page import login_modal_class
from POM.home_page import Homepage_class


#to copy driver lines in all codes
@pytest.fixture(scope="function")
def driverInstance():
    chromium_path = r"C:\Users\ujala.rehan\Desktop\selenium\chrome-win64\chrome.exe"  
    options = Options()
    options.binary_location = chromium_path
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10) 
    yield driver
    driver.quit()

@pytest.fixture
def open_sign_up_modal(driverInstance):
    driver=driverInstance #all driver related code in conftest file
    driver.get("https://www.demoblaze.com/")
    driver.maximize_window()
    driver.implicitly_wait(5) 
    register_modal = reg_modal_class(driver)
    register_modal.sign_up_modal()
    return register_modal
    
@pytest.fixture
def open_login_modal(driverInstance):
    driver=driverInstance #all driver related code in conftest file
    driver.get("https://www.demoblaze.com/")
    driver.maximize_window()
    driver.implicitly_wait(5) 
    login = login_modal_class(driver)
    login.login_modal()
    return login
    
@pytest.fixture
def go_to_homepage(driverInstance):
    driver=driverInstance #all driver related code in conftest file
    driver.get("https://www.demoblaze.com/")
    return Homepage_class(driver)
   