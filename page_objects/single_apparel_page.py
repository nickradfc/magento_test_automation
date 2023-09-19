from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
import re


class SingleApparelPage(BasePage):
    APPAREL_NAME = {
        "locator": (By.XPATH, '//*[@data-ui-id="page-title-wrapper"]'),
    }

    SIZES = {
        "locator": (By.CSS_SELECTOR, f'[id^="option-label-size-"]')
    }

    COLORS = {
        "locator": (By.CSS_SELECTOR, f'[id^="option-label-color-"]')
    }

    QUANTITY = {
        "locator": (By.ID, "qty")
    }

    ADD_TO_CART_BTN = {
        "locator": (By.ID, "product-addtocart-button"),
        "text": "Add to Cart"
    }

    CART_ITEMS_QTY_COUNTER = {
        "locator": (By.XPATH, "/html/body/div[2]/header/div[2]/div[1]/a/span[2]/span[1]"),
    }

    ADDED_TO_CART_SUCCESS_BANNER = {
        "locator": (By.XPATH, '//*[@data-ui-id="message-success"]'),
    }

    def assert_item_name(self, name):
        self.find_element(self.APPAREL_NAME["locator"])
        self.assert_text_in_element(self.APPAREL_NAME["locator"], name)

    def get_option(self, spec, required_option):
        # method to get required spec option: size or color elmenet to select
        specs_map = {
            "size": self.SIZES["locator"],
            "color": self.COLORS["locator"]
        }
        all_options = self.find_elements(specs_map[spec])
        for option in all_options:
            if option.get_attribute("option-label") == required_option:
                return option

    def select_option(self, opt, opt_to_select):
        option = self.get_option(opt, opt_to_select)
        option.click()

    def verify_option_selected(self, opt, opt_to_select):
        option = self.get_option(opt, opt_to_select)
        checked = option.get_attribute("aria-checked")
        assert checked == "true"

    def type_quantity(self, qty):
        qty_field = self.find_element(self.QUANTITY["locator"])
        qty_field.clear()
        qty_field.send_keys(qty)

    def assert_qty(self, qty):
        qty_field = self.find_element(
            self.QUANTITY["locator"]).get_attribute("value")
        assert int(
            qty_field) == qty, f"Quantity mismatch actual: {qty_field} - expected: {qty}"

    def click_add_to_cart_btn(self):
        self.assert_text_in_element(
            self.ADD_TO_CART_BTN["locator"], self.ADD_TO_CART_BTN["text"])
        self.find_element(self.ADD_TO_CART_BTN["locator"]).click()

    def assert_cart_counter(self, qty):
        self.assert_text_in_element(
            self.CART_ITEMS_QTY_COUNTER["locator"], str(qty))
        cart_counter = self.find_element(
            self.CART_ITEMS_QTY_COUNTER["locator"])
        assert int(cart_counter.text) == qty, "Cart quantity mismatch"

    def item_added_success_banner(self):
        self.is_visible(self.ADDED_TO_CART_SUCCESS_BANNER["locator"])
        self.assert_regex_in_element(
            self.ADDED_TO_CART_SUCCESS_BANNER["locator"], r"You added (.+?) to your")

    def click_banner_shpopping_cart(self):
        banner = self.find_element(
            self.ADDED_TO_CART_SUCCESS_BANNER["locator"])
        banner.find_element(By.TAG_NAME, "a").click()
