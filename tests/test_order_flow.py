import pytest
from utilities.driver_manager import get_chrome_driver
# This is a custom utility to read .env variables
from utilities.env_reader import read_env_variable
from page_helpers.main_landing_page_helper import navigate_to_sign_up
from page_helpers.sign_up_page_helper import sign_up
from page_helpers.my_account_page_helper import verify_registration_banner


@pytest.fixture(scope="module")
def driver():
    driver = get_chrome_driver()
    yield driver
    driver.quit()


def test_sign_in(driver):
    # Load sign-in credentials from .env file
    signin_email = read_env_variable("MAGENTO_REGISTERED_EMAIL")
    signin_password = read_env_variable("MAGENTO_REGISTERED_PASSWORD")

    # Step 1: Navigate to the main landing page
    driver.get("https://magento.softwaretestingboard.com/")

    # Step 2: Navigate to the sign-in page
    navigate_to_sign_up(driver)

    # Step 3: Sign in
    sign_up(driver)

    # Step 3: Verify registration is successful
    verify_registration_banner(driver)
