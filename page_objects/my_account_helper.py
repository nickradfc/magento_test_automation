from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class MyAccountPage(BasePage):

    SUCCESSFUL_REGESTRATION_BANNER = {
        "locator": (By.XPATH, '//*[@id="maincontent"]/div[1]/div[2]/div/div/div'),
        "text": "Thank you for registering with Main Website Store."
    }

    def assert_successful_registration_banner(self):
        self.find_element(self.SUCCESSFUL_REGESTRATION_BANNER["locator"])
        self.assert_text_in_element(
            self.SUCCESSFUL_REGESTRATION_BANNER["locator"], self.SUCCESSFUL_REGESTRATION_BANNER["text"])
