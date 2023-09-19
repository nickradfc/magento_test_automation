# In your conftest.py
import pytest
from utilities.env_reader import read_env_variable
from utilities.general_utils import generate_random_email
from fixtures.test_data_fixture import SIGN_UP_FIRST_NAME, SIGN_UP_LAST_NAME


@pytest.fixture(scope="module")
def sign_up_creds():
    base_email = read_env_variable("BASE_EMAIL")
    signup_email = generate_random_email(base_email)
    signup_password = read_env_variable("BASE_PASSWORD")

    global sign_up_creds
    sign_up_creds = {
        "email": signup_email,
        "password": signup_password,
        "firstname": SIGN_UP_FIRST_NAME,
        "lastname": SIGN_UP_LAST_NAME,
        "street": "Best test street #1",
        "city": "Test Automation City",
        "postcode": "12345",
        "telephone": "1234567890",
        "state": "California"
    }
    return sign_up_creds
