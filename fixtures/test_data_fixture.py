import pytest
from utilities.env_reader import read_env_variable
from utilities.general_utils import generate_random_email

SIGN_UP_FIRST_NAME = "James"
SIGN_UP_LAST_NAME = "BOND"

@pytest.fixture
def sign_up_creds():
    base_email = read_env_variable("MAGENTO_REGISTERED_EMAIL")
    signup_email = generate_random_email(base_email)
    signup_password = read_env_variable("MAGENTO_REGISTERED_PASSWORD")

    credentials = {
        "email": signup_email,
        "password": signup_password,
        "first_name": SIGN_UP_FIRST_NAME,
        "last_name": SIGN_UP_LAST_NAME
    }
    return credentials
