from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from config import DEFAULT_WAIT_TIME


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.default_wait_time = DEFAULT_WAIT_TIME

    def assert_text_in_element(self, locator, expected_txt, seconds=DEFAULT_WAIT_TIME):
        wait = WebDriverWait(self.driver, seconds)  # Use self.driver, not self
        wait.until(EC.text_to_be_present_in_element(
            locator, expected_txt))

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        element.location_once_scrolled_into_view

    def find_element(self, by_locator):
        element = WebDriverWait(self.driver, self.default_wait_time).until(
            EC.presence_of_element_located(by_locator)
        )
        return element

    def click(self, by_locator):
        self.scroll_to_element(by_locator)
        self.find_element(by_locator).click()

    def enter_text(self, by_locator, text):
        self.scroll_to_element(by_locator)
        self.find_element(by_locator).send_keys(text)

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, self.default_wait_time).until(
            EC.visibility_of_element_located(by_locator)
        )
        return bool(element)

    def is_clickable(self, by_locator):
        element = WebDriverWait(self.driver, self.default_wait_time).until(
            EC.element_to_be_clickable(by_locator)
        )
        return bool(element)

    def get_text(self, by_locator):
        element = self.find_element(by_locator)
        return element.text

    def is_exists(self, by_locator):
        try:
            self.find_element(by_locator)
            return True
        except:
            return False

    def assert_element(self, locator):
        return self.is_visible(locator) and self.is_clickable(locator)

    def assert_typable(self, locator):
        return self.assert_element(locator) and self.is_typable(locator)

    def is_visible(self, locator):
        element = self.driver.find_element(*locator)
        return element.is_displayed()

    def is_clickable(self, locator):
        element = self.driver.find_element(*locator)
        return element.is_enabled()

    def is_typable(self, locator):
        element = self.driver.find_element(*locator)
        return 'readonly' not in element.get_attribute('outerHTML')
