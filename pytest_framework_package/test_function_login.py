import json
import pytest
#tests 1-5 run with data present in json file
# 1. login with valid data
# 2. 
# 3. Error message on empty form submission
# 4. Error message when username is empty
# 5. Error message when password is empty

with open("../json_data_files/login_data.json") as f:
    test_cases = json.load(f)["login_test_cases"]

@pytest.mark.parametrize("case", test_cases )
def test_credentials(open_login_modal, case):
    open_login_modal.valid_username(case["input"]["username"])
    open_login_modal.valid_password(case["input"]["password"])#from pom

    open_login_modal.button_clicking(open_login_modal.login_button)#from utils
    
    alert = open_login_modal.wait_for_alert()
    alertText = alert.text
    print(alertText)
    assert case["expected_result"] in alertText
    alert.accept()
    
    open_login_modal.button_clicking(open_login_modal.logout_button)#from utils

# 6. Verify form resets after closing modal
@pytest.mark.parametrize("case", test_cases )
def test_form_reset(open_login_modal, case):
    open_login_modal.valid_username(case["input"]["username"])
    open_login_modal.valid_password(case["input"]["password"])
    open_login_modal.button_clicking(open_login_modal.login_button)
    
    alert = open_login_modal.wait_for_alert()
    alert.accept()

    assert open_login_modal.form_reset_validation() == ""

   

        

