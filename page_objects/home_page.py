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

    CATEGORY_PAGE_TITLE = {
        "locator": (By.XPATH, '//*[@data-ui-id="page-title-wrapper"]'),
    }

    WOMEN_CATEGORY = {
        "locator": (By.ID, "ui-id-4"),
        "text": "Women"
    }

    JACKETS_CATEGORY = {
        "locator": (By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div[2]/div/ul[1]/li[2]/a'),
        "text": "Jackets"
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
        
    def select_women_category(self):    
        self.find_element(self.WOMEN_CATEGORY["locator"])
        self.assert_text_in_element(self.WOMEN_CATEGORY["locator"], self.WOMEN_CATEGORY["text"])
        self.click(self.WOMEN_CATEGORY["locator"])

    def assert_category_page_title(self, category):
        self.find_element(self.CATEGORY_PAGE_TITLE["locator"])
        self.is_visible(self.CATEGORY_PAGE_TITLE["locator"])
        self.assert_text_in_element(self.CATEGORY_PAGE_TITLE["locator"], category)
        

    def select_jacket_category(self):
        # Jackets category has the same locator for women and men categories.
        self.find_element(self.JACKETS_CATEGORY["locator"])
        self.assert_text_in_element(self.JACKETS_CATEGORY["locator"], self.JACKETS_CATEGORY["text"])
        self.click(self.JACKETS_CATEGORY["locator"])
        
    def assert_apparel_category_page_title(self, apparely_category):
        pass
        # self.find_element(self.CATEGORY_PAGE_TITLE["locator"])
        # self.is_visible(self.CATEGORY_PAGE_TITLE["locator"])
        # self.assert_text_in_element(self.CATEGORY_PAGE_TITLE["locator"], category)