import json
import pytest

with open("../json_data_files/data.json") as f:
    test_cases = json.load(f)["registration_test_cases"]

@pytest.mark.parametrize("case", test_cases )
def test_credentials(open_sign_up_modal, case):
    open_sign_up_modal.valid_username(case["input"]["username"])
    open_sign_up_modal.valid_password(case["input"]["password"])
    open_sign_up_modal.button_clicking(open_sign_up_modal.signup_register_button)
    
    alert = open_sign_up_modal.wait_for_alert()
    alertText = alert.text
    print(alertText)
    assert case["expected_result"] in alertText
    alert.accept()


        

