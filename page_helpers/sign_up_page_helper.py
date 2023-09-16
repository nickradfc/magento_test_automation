from page_objects.sign_up_page import SignUpPage
from utilities.general_utils import generate_random_email
from utilities.env_reader import read_env_variable
from fixtures.test_data_fixture import SIGN_UP_FIRST_NAME, SIGN_UP_LAST_NAME


def sign_up(driver):
    base_email = read_env_variable("MAGENTO_REGISTERED_EMAIL")
    signup_password = read_env_variable("MAGENTO_REGISTERED_PASSWORD")
    signup_email = generate_random_email(base_email)

    sign_up_page = SignUpPage(driver)
    sign_up_page.enter_first_name(SIGN_UP_FIRST_NAME)
    sign_up_page.enter_last_name(SIGN_UP_LAST_NAME)
    sign_up_page.enter_email(signup_email)
    sign_up_page.enter_password(signup_password)
    sign_up_page.enter_confirm_password(signup_password)
    sign_up_page.click_create_account()
