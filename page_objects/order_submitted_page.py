from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
import re


class OrderSubmittedPage(BasePage):
    PAGE_TITLE = {
        "locator": (By.XPATH, '//*[@data-ui-id="page-title-wrapper"]'),
        "text": "Thank you for your purchase!"
    }

    ORDER_NUMBER_CONFIRMATION = {
        "locator": (By.XPATH, '//*[@id="maincontent"]/div[3]/div/div[2]'),
        "text": ""
    }

    def check_order_confirmation_title(self):
        self.assert_text_in_element(
            self.PAGE_TITLE["locator"], self.PAGE_TITLE["text"])

    def check_order_number(self):
        regex = r"Your order number is: \d+."
        self.assert_regex_in_element(
            self.ORDER_NUMBER_CONFIRMATION["locator"], regex)
