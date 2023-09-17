import pytest
from utilities.driver_manager import get_chrome_driver
from page_helpers.main_landing_page_helper import navigate_to_sign_up, navigate_to_sign_in
from page_helpers.sign_up_page_helper import sign_up
from page_helpers.sign_in_page_helper import sign_in
from fixtures.test_data_fixture import SIGN_UP_FIRST_NAME, SIGN_UP_LAST_NAME
from fixtures.test_data_fixture import sign_up_creds
from page_helpers.home_page_helper import verify_welcome_message, select_main_category, select_apparel
from page_helpers.apparel_selection_page_helper import select_item_by_index, get_apparel_name_by_index
from page_helpers.single_apparel_page_helper import verify_apparel_page_name

@pytest.fixture(scope="module")
def driver():
    driver = get_chrome_driver()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def before_each(request, driver):
    driver.get("https://magento.softwaretestingboard.com/")
    # Ensure that cookies and local storage are cleared after the test
    def clear_cookies_and_storage():
        driver.delete_all_cookies()
        driver.execute_script("localStorage.clear();")
    request.addfinalizer(clear_cookies_and_storage)

def test_sign_up(driver, before_each, sign_up_creds):
    navigate_to_sign_up(driver)
    sign_up(driver, sign_up_creds)

def test_sign_in_with_new_user(driver, before_each, sign_up_creds):
    navigate_to_sign_in(driver)
    # sign_in(driver, sign_up_creds["email"], sign_up_creds["password"])
    sign_in(driver, "nickradfc+test@gmail.com", "Test111@")
    verify_welcome_message(driver)

def test_select_main_category(driver):
    select_main_category(driver, 'Women')

def test_select_apparel_category(driver):
    apparel_category = "Jackets"
    select_apparel(driver, apparel_category)

def test_select_item(driver):
    item_index = 1
    item_name = get_apparel_name_by_index(driver, item_index)
    select_item_by_index(driver, item_index)
    verify_apparel_page_name(driver, item_name)