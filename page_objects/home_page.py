from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class HomePage(BasePage):

    WELCOME_MESSAGE = {
        "locator": (By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[1]/span"),
        "text": "Welcome, "
    }

    CUSTOMER_MENU_TOGGLE = {
        "locator": (By.XPATH, '//*[@data-action="customer-menu-toggle"]'),
    }

    MY_ACCOUNT_BUTTON = {
        "locator": (By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[2]/div/ul/li[1]/a'),
        "text": "My Account"
    }

    def check_welcome_message(self):
        self.assert_element(self.WELCOME_MESSAGE["locator"])
        self.assert_text_in_element(
            self.WELCOME_MESSAGE["locator"], self.WELCOME_MESSAGE["text"])

    def click_customer_menu_toggle(self):
        self.click(self.CUSTOMER_MENU_TOGGLE["locator"])

    def assert_my_account_btn_text(self):
        self.assert_element(self.MY_ACCOUNT_BUTTON["locator"])
        self.assert_text_in_element(self.MY_ACCOUNT_BUTTON["locator"], self.MY_ACCOUNT_BUTTON["text"])

    def click_my_account_btn(self):
        self.assert_element(self.MY_ACCOUNT_BUTTON["locator"])
        self.click(self.MY_ACCOUNT_BUTTON["locator"])
        

        import pdb; pdb.set_trace()
