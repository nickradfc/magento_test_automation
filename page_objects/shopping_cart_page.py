from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
import re


class ShoppingCartPage(BasePage):
    PAGE_TITLE = {
        "locator": (By.XPATH, '//*[@data-ui-id="page-title-wrapper"]'),
        "text": "Shopping Cart"
    }

    ITEM_SPECS = {
        "locator": (By.XPATH, '//*[@id="shopping-cart-table"]/tbody/tr[1]/td[1]/div'),
    }

    PROCEED_TO_CHECKOUT_BTN = {
        "locator": (By.XPATH, '//*[@id="maincontent"]/div[3]/div/div[2]/div[1]/ul/li[1]/button'),
        "text": "Proceed to Checkout"
    }

    def assert_page_title(self):
        self.is_visible(self.PAGE_TITLE["locator"])
        self.assert_text_in_element(
            self.PAGE_TITLE["locator"], self.PAGE_TITLE["text"])

    def verify_item_spec(self, spec):
        assert spec in self.find_element(
            self.ITEM_SPECS["locator"]).text, f"Item spec {spec} not in item description"

    def click_proceed_to_checkout(self):
        self.is_visible(self.PROCEED_TO_CHECKOUT_BTN["locator"])
        self.assert_text_in_element(
            self.PROCEED_TO_CHECKOUT_BTN["locator"], self.PROCEED_TO_CHECKOUT_BTN["text"])
        self.click(self.PROCEED_TO_CHECKOUT_BTN["locator"])
