from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from selenium.webdriver.support.ui import Select


class ShippingAddressFormPage(BasePage):
    PAGE_TITLE = {
        "locator": (By.XPATH, '//*[@id="shipping"]/div[1]'),
        "text": "Shipping Address"
    }

    SHIPPING_FORM = {
        "locator": (By.CLASS_NAME, "checkout-shipping-address"),
    }

    INPUT_FIELDS = {
        "locator": (By.TAG_NAME, "input"),
    }

    SELECT_ELEMENTS = {
        "locator": (By.TAG_NAME, "select"),
    }

    OPTION_ELEMENTS = {
        "locator": (By.TAG_NAME, "option"),
    }

    SHIPPING_METHODS_SECTION = {
        "locator": (By.ID, "checkout-shipping-method-load")
    }

    NEXT_BUTTON = {
        "locator": (By.XPATH, '//*[@id="shipping-method-buttons-container"]/div/button'),
        "text": "Next"
    }

    def assert_page_title(self):
        self.find_element(self.PAGE_TITLE["locator"])
        self.assert_text_in_element(
            self.PAGE_TITLE["locator"], self.PAGE_TITLE["text"])

    def set_input_field_value(self, field_name, first_name):
        all_fields = self.find_elements(self.INPUT_FIELDS["locator"])
        for field in all_fields:
            if field.get_attribute("name") == field_name:
                self.scroll_to_element(field)
                field.clear()
                field.send_keys(first_name)

    def get_all_select_elements(self):
        return self.find_elements(self.SELECT_ELEMENTS["locator"])

    def get_all_option_elements(self):
        return self.find_elements(self.OPTION_ELEMENTS["locator"])

    def select_state(self, state):
        all_select_elements = self.get_all_select_elements()
        for el in all_select_elements:
            if el.get_attribute("name") == "region_id":
                dropdown = Select(el)
                dropdown.select_by_visible_text(state)

    def select_shipping_option(self):
        # since there is not test requirement around shipping options, selecting first available option
        shipping_method_section = self.find_element(
            self.SHIPPING_METHODS_SECTION["locator"])
        assert shipping_method_section is not None, "Error selecting shipping options"
        shipping_method_section.find_elements(By.TAG_NAME, "input")[0].click()

    def click_next_btn(self):
        self.scroll_to_element(self.NEXT_BUTTON["locator"])
        self.find_element(self.NEXT_BUTTON["locator"]).click()

    def verify_next_btn_text(self):
        self.assert_text_in_element(
            self.NEXT_BUTTON["locator"], self.NEXT_BUTTON["text"])
