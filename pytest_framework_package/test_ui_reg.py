#TEST 1: Verify modal opens
# functions taken from POM
def test_sign_up_modal(open_sign_up_modal): 
    assert open_sign_up_modal.get_modal_heading() == "Sign up"

#TEST 2: Verify Username and Password fields are visible
# functions taken from POM
def test_fields_are_visible(open_sign_up_modal):
    assert open_sign_up_modal.field_visible()

#TEST 3: Verify Username and Password fields are clickabale
# functions taken from POM
def test_fields_are_clickable(open_sign_up_modal):  
    assert open_sign_up_modal.fileds_clickable()

#Test 4: Verify Close button visible and clickable 
# functions taken from utils
def test_Close_button_visible_and_clickable(open_sign_up_modal):
    assert open_sign_up_modal.is_visible(open_sign_up_modal.signup_close_button)
    assert open_sign_up_modal.is_clickable(open_sign_up_modal.signup_close_button)

#Test 5: Verify Sign_up button visible and clickable 
# functions taken from utils
def test_sign_up_button_visible_and_clickable(open_sign_up_modal):
    assert open_sign_up_modal.is_visible(open_sign_up_modal.signup_register_button)
    assert open_sign_up_modal.is_clickable(open_sign_up_modal.signup_register_button)

#Test 6: Verify password masking
def test_password_mask(open_sign_up_modal):
    assert open_sign_up_modal.password_masking_check() is True
    


   
    



   

