import json
import pytest

#tests 1-5 run with data present in json file
# 1. Submit form with valid data
# 2. Submit form with existing username (duplicate user)
# 3. Error message on empty form submission
# 4. Error message when username is empty
# 5. Error message when password is empty

with open("../json_data_files/data.json") as f:
    test_cases = json.load(f)["registration_test_cases"]

@pytest.mark.parametrize("case", test_cases )
def test_signup_credentials(open_sign_up_modal, case):
    open_sign_up_modal.valid_username(case["input"]["username"])
    open_sign_up_modal.valid_password(case["input"]["password"])
    open_sign_up_modal.button_clicking(open_sign_up_modal.signup_register_button)
    
    alert = open_sign_up_modal.wait_for_alert()
    alertText = alert.text
    print(alertText)
    assert case["expected_result"] in alertText
    alert.accept()

# 6. Verify form resets after closing modal

#@pytest.mark.parametrize("case", test_cases )
def test_form_reset(open_sign_up_modal, case):
    case = test_cases[0]  # only run valid case

    # Step 1: Enter valid data
    open_sign_up_modal.valid_username(case["input"]["username"])
    open_sign_up_modal.valid_password(case["input"]["password"])

    # Step 2: Click register
    open_sign_up_modal.button_clicking(open_sign_up_modal.signup_register_button)

    # Step 3: Handle alert
    alert = open_sign_up_modal.wait_for_alert()
    alert.accept()

    # Step 4: Close modal
    open_sign_up_modal.button_clicking(open_sign_up_modal.signup_close_button)
   
    open_sign_up_modal.sign_up_modal()

    # Step 6: Assert reset
    assert open_sign_up_modal.form_reset_validation() == {"username": "validyuser", "password": "Valid_123"}



        

