from page_objects.shipping_address_form_page import ShippingAddressFormPage


def verify_shipping_info_page_title(driver):
    shipping_address_page = ShippingAddressFormPage(driver)
    shipping_address_page.assert_page_title()


def populate_shipping_form_input_fields(driver, field_name, field_value):
    shipping_address_page = ShippingAddressFormPage(driver)
    shipping_address_page.set_input_field_value(field_name, field_value)


def select_shipping_state(driver, state):
    shipping_address_page = ShippingAddressFormPage(driver)
    shipping_address_page.select_state(state)


def select_shipping_method(driver):
    shipping_address_page = ShippingAddressFormPage(driver)
    shipping_address_page.select_shipping_option()


def proceed_to_order_preview(driver):
    shipping_address_page = ShippingAddressFormPage(driver)
    shipping_address_page.verify_next_btn_text()
    shipping_address_page.click_next_btn()
