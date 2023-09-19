from page_objects.sign_up_page import SignUpPage
from utilities.env_reader import read_env_variable


def sign_up(driver, creds):
    sign_up_page = SignUpPage(driver)
    sign_up_page.enter_first_name(creds["firstname"])
    sign_up_page.enter_last_name(creds["lastname"])
    sign_up_page.enter_email(creds["email"])
    sign_up_page.enter_password(creds["password"])
    sign_up_page.enter_confirm_password(creds["password"])
    sign_up_page.click_create_account()
