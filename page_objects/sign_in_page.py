from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class SignInPage(BasePage):

    SIGN_IN_FORM_HEADER = {
        "locator": (By.XPATH, '//*[@data-ui-id="page-title-wrapper"]'),
        "text": "Customer Login"
    }
    EMAIL_FIELD = {
        "locator": (By.ID, 'email'),
    }
    PASSWORD_FIELD = {
        "locator": (By.ID, 'pass'),
    }
    SIGN_IN_BUTTON = {
        "locator": (By.ID, "send2"),
    }

    def assert_form_header(self):
        header = self.find_element(self.SIGN_IN_FORM_HEADER["locator"])
        assert header.text == self.SIGN_IN_FORM_HEADER["text"], f"Sign in form header text mismatch."

    def enter_email(self, email):
        self.assert_typable(self.EMAIL_FIELD["locator"])
        self.enter_text(self.EMAIL_FIELD["locator"], email)

    def enter_password(self, password):
        self.assert_typable(self.PASSWORD_FIELD["locator"])
        self.enter_text(self.PASSWORD_FIELD["locator"], password)

    def click_sign_in(self):
        self.assert_element(self.SIGN_IN_BUTTON["locator"])
        self.click(self.SIGN_IN_BUTTON["locator"])
