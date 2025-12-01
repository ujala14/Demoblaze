#TEST 1: Verify login modal opens
# functions taken from POM
def test_login_modal(open_login_modal): 
    assert open_login_modal.get_login_modal_heading() == "Log in"

#TEST 2: Verify Username and Password fields are visible
# functions taken from POM
def test_login_fields_are_visible(open_login_modal):
    assert open_login_modal.login_field_visible()

#TEST 3: Verify Username and Password fields are clickabale
# functions taken from POM
def test_fields_are_clickable(open_login_modal):  
    assert open_login_modal.login_fields_clickable()

#Test 4: Verify Close button visible and clickable 
# functions taken from utils
def test_Close_button_visible_and_clickable(open_login_modal):
    assert open_login_modal.is_visible(open_login_modal.login_close_button)
    assert open_login_modal.is_clickable(open_login_modal.login_close_button)

#Test 5: Verify Sign_in button visible and clickable 
# functions taken from utils
def test_sign_up_button_visible_and_clickable(open_login_modal):
    assert open_login_modal.is_visible(open_login_modal.login_button)
    assert open_login_modal.is_clickable(open_login_modal.login_button)

#Test 6: Verify password masking
def test_password_mask(open_login_modal):
    assert open_login_modal.password_masking_check() is True

    


   
    



   

