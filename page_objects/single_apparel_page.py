from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class SingleApparelPage(BasePage):
    APPAREL_NAME = {
        "locator": (By.XPATH, '//*[@data-ui-id="page-title-wrapper"]'),
    }

    def assert_item_name(self, name):
        self.find_element(self.APPAREL_NAME["locator"])
        self.assert_text_in_element(self.APPAREL_NAME["locator"], name)
