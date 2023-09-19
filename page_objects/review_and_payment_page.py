from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
import re


class ReviewAndPaymentPage(BasePage):
    BILLING_CHECKBOX = {
        "locator": (By.ID, 'billing-address-same-as-shipping-checkmo'),
    }

    ORDER_SUMMARY = {
        "locator": (By.XPATH, '//*[@id="opc-sidebar"]/div[1]'),
    }

    PLACE_ORDER_BTN = {
        "locator": (By.XPATH, '//*[@id="checkout-payment-method-load"]/div/div/div[2]/div[2]/div[4]/div/button'),
        "text": "Place Order"
    }

    def check_billing_checkbox_selected(self):
        checkbox = self.find_element(self.BILLING_CHECKBOX["locator"])
        if not checkbox.is_selected():
            checkbox.click()

    def check_order_summary_info(self):
        # since there is no test requirement around this verification, just varifying that the total order amount is not $0.00
        regex = r"Subtotal \$\d+.\d+"
        summary_info = self.find_element(self.ORDER_SUMMARY["locator"]).text
        match = re.search(regex, summary_info)

        if match:
            total_amount = match.group(0)
            if total_amount == "$0.00":
                raise f"Review and payment total amount is $0.00: {total_amount}"

    def click_place_order(self):
        self.assert_element(self.PLACE_ORDER_BTN["locator"])
        self.assert_text_in_element(
            self.PLACE_ORDER_BTN["locator"], self.PLACE_ORDER_BTN["text"])
        self.click(self.PLACE_ORDER_BTN["locator"])
