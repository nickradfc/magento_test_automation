from page_objects.sign_in_page import SignInPage

def sign_in(driver, email, password):
    sign_in_page = SignInPage(driver)
    sign_in_page.assert_form_header()
    sign_in_page.enter_email(email)
    sign_in_page.enter_password(password)
    sign_in_page.click_sign_in()
