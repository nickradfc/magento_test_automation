from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class SignUpPage(BasePage):

    FIRST_NAME_FIELD = {
        "locator": (By.ID, "firstname")
    }
    LAST_NAME_FIELD = {
        "locator": (By.ID, "lastname")
    }
    EMAIL_FIELD = {
        "locator": (By.ID, "email_address")
    }
    PASSWORD_FIELD = {
        "locator": (By.ID, "password")
    }
    CONFIRM_PASSWORD_FIELD = {
        "locator": (By.ID, "password-confirmation")
    }
    CREATE_ACCOUNT_BUTTON = {
        "locator": (By.XPATH, '//*[@id="form-validate"]/div/div[1]/button')
    }

    def enter_first_name(self, first_name):
        self.assert_typable(self.FIRST_NAME_FIELD["locator"])
        self.enter_text(self.FIRST_NAME_FIELD["locator"], first_name)

    def enter_last_name(self, last_name):
        self.assert_typable(self.LAST_NAME_FIELD["locator"])
        self.enter_text(self.LAST_NAME_FIELD["locator"], last_name)

    def enter_email(self, email):
        self.assert_typable(self.EMAIL_FIELD["locator"])
        self.enter_text(self.EMAIL_FIELD["locator"], email)

    def enter_password(self, password):
        self.assert_typable(self.PASSWORD_FIELD["locator"])
        self.enter_text(self.PASSWORD_FIELD["locator"], password)

    def enter_confirm_password(self, confirm_password):
        self.assert_typable(self.CONFIRM_PASSWORD_FIELD["locator"])
        self.enter_text(
            self.CONFIRM_PASSWORD_FIELD["locator"], confirm_password)

    def click_create_account(self):
        self.assert_element(self.CREATE_ACCOUNT_BUTTON["locator"])
        self.click(self.CREATE_ACCOUNT_BUTTON["locator"])
