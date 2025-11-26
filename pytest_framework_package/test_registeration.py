#TEST 1: Verify modal opens
def test_sign_up_modal(open_sign_up_modal): 
    assert open_sign_up_modal.get_modal_heading() == "Sign up"

#TEST 2: Verify Username and Password fields are visible
def test_fields_are_visible(open_sign_up_modal):
    assert open_sign_up_modal.is_element_visible(open_sign_up_modal.field_username)
    assert open_sign_up_modal.is_element_visible(open_sign_up_modal.field_password)

#TEST 3: Verify Username and Password fields are clickabale
def test_fields_are_clickable(open_sign_up_modal):  
    assert open_sign_up_modal.fields_are_clickable(open_sign_up_modal.field_username)
    assert open_sign_up_modal.is_clickable(open_sign_up_modal.field_password)

#Test 4: Verify Close button visible and clickable 
def test_Close_button_visible_and_clickable(open_sign_up_modal):
    assert open_sign_up_modal.is_element_visible(open_sign_up_modal.signup_close_button)
    assert open_sign_up_modal.is_clickable(open_sign_up_modal.signup_close_button)

#Test 5: Verify Sign_up button visible and clickable 
def test_sign_up_button_visible_and_clickable(open_sign_up_modal):
    assert open_sign_up_modal.is_element_visible(open_sign_up_modal.signup_register_button)
    assert open_sign_up_modal.is_clickable(open_sign_up_modal.signup_register_button)



    


   
    



   

