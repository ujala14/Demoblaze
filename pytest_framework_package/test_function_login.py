import json
import pytest

with open("../json_data_files/login_data.json") as f:
    data = json.load(f)

valid_cases = data["valid_login_cases"]
invalid_cases = data["invalid_cases"]

@pytest.mark.parametrize("case", valid_cases)
def test_valid_login(open_login_modal, case):
    open_login_modal.valid_login_username(case["input"]["username"])
    open_login_modal.valid_login_password(case["input"]["password"])
    open_login_modal.button_clicking(open_login_modal.login_button)
 
 # Verify navbar text
    msg = open_login_modal.get_welcome_message()
    assert case["expected_result"] in msg
    print(msg)
    open_login_modal.button_clicking(open_login_modal.logout_button)

# cases_to_run = [case for case in invalid_cases if case["id"] in [5, 6]] #for selected cases 
@pytest.mark.parametrize("case", invalid_cases)
def test_invalid_logins(open_login_modal, case):
   open_login_modal.valid_login_username(case["input"]["username"])
   open_login_modal.valid_login_password(case["input"]["password"])

   open_login_modal.button_clicking(open_login_modal.login_button)#from utils
    
   alert = open_login_modal.wait_for_alert()
   alertText = alert.text
   print(alertText)
   assert case["expected_result"] in alertText
   alert.accept()


   

        

