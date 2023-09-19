import pytest
from page_helpers.main_landing_page_helper import navigate_to_sign_up, navigate_to_sign_in
from page_helpers.sign_up_page_helper import sign_up
from page_helpers.sign_in_page_helper import sign_in
from utilities.driver_manager import get_chrome_driver
from fixtures.test_data_fixture import SIGN_UP_FIRST_NAME, SIGN_UP_LAST_NAME
from fixtures.test_data_fixture import item_specs
from conftest import sign_up_creds
from page_helpers.home_page_helper import verify_welcome_message, select_main_category, select_apparel
from page_helpers.apparel_selection_page_helper import select_item_by_index, get_apparel_name_by_index
from page_helpers.single_apparel_page_helper import verify_apparel_page_name, select_item_spec, verify_spec_selected, select_quantity, verify_quantity_set, add_to_cart, verify_item_added_banner, open_cart_from_banner
from page_helpers.shopping_cart_page_helper import verify_page_title, verify_cart_item_description, proceed_to_checkout
from page_helpers.shipping_address_form_page_helper import populate_shipping_form_input_fields, verify_shipping_info_page_title, select_shipping_state, select_shipping_method, proceed_to_order_preview
from page_helpers.review_and_payment_page_helper import verify_billing_and_submit
from page_helpers.order_submitted_page_helper import verify_order_placed


@pytest.fixture(scope="module")
def driver():
    driver = get_chrome_driver()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def before(request, driver):
    driver.get("https://magento.softwaretestingboard.com/")


def test_sign_up(driver, before, sign_up_creds):
    navigate_to_sign_up(driver)
    sign_up(driver, sign_up_creds)
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


def test_select_item_specs(driver, item_specs):
    select_item_spec(driver, "size", item_specs["size"])
    verify_spec_selected(driver, "size", item_specs["size"])
    select_item_spec(driver, "color", item_specs["color"])
    verify_spec_selected(driver, "color", item_specs["color"])


def test_select_color(driver, item_specs):
    select_quantity(driver, item_specs["qty"])
    verify_quantity_set(driver, item_specs["qty"])


def test_add_item_to_cart(driver, item_specs):
    add_to_cart(driver, item_specs["qty"])


def test_proceed_checkout(driver, item_specs):
    verify_item_added_banner(driver)
    open_cart_from_banner(driver)
    verify_page_title(driver)
    verify_cart_item_description(driver, item_specs)
    proceed_to_checkout(driver)


def test_populate_shipping_address(driver, sign_up_creds):
    verify_shipping_info_page_title(driver)
    populate_shipping_form_input_fields(
        driver, "firstname", sign_up_creds["firstname"])
    populate_shipping_form_input_fields(
        driver, "lastname", sign_up_creds["lastname"])
    populate_shipping_form_input_fields(
        driver, "street[0]", sign_up_creds["street"])
    populate_shipping_form_input_fields(driver, "city", sign_up_creds["city"])
    populate_shipping_form_input_fields(
        driver, "telephone", sign_up_creds["telephone"])
    populate_shipping_form_input_fields(
        driver, "postcode", sign_up_creds["postcode"])
    # this logic assumes that we test US address only
    select_shipping_state(driver, sign_up_creds["state"])
    select_shipping_method(driver)
    proceed_to_order_preview(driver)


def test_place_order(driver):
    verify_billing_and_submit(driver)    
    verify_order_placed(driver)

