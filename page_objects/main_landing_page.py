from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class MainLandingPage(BasePage):

    SIGN_IN_BUTTON = {
        "locator": (By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[2]/a"),
        "text": "Sign In"
    }
    SIGN_UP_BUTTON = {
        "locator": (By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[3]/a"),
        "text": "Create an Account"
    }

    def navigate_to_sign_in(self):
        self.assert_element(self.SIGN_IN_BUTTON["locator"])
        self.assert_text_in_element(
            self.SIGN_IN_BUTTON["locator"], self.SIGN_IN_BUTTON["text"])
        self.click(self.SIGN_IN_BUTTON["locator"])

    def navigate_to_sign_up(self):
        self.assert_element(self.SIGN_UP_BUTTON["locator"])
        self.assert_text_in_element(
            self.SIGN_UP_BUTTON["locator"], self.SIGN_UP_BUTTON["text"])
        self.click(self.SIGN_UP_BUTTON["locator"])
