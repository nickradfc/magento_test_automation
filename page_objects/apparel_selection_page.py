from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class ApparelSelectionPage(BasePage):
    PARENT_ELEMENT = {
        "locator": (By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol'),
    }
    ALL_ITEMS = {
        "locator": 'li',
    }

    ITEM_NAME = {
        "locator": '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[2]/div/div/strong/a',
    }

    def select_item_by_index(self, driver, ind):
        li_elements = self.get_list_of_all_items()
        self.click(li_elements[ind], driver)

    def get_list_of_all_items(self):
        # Find the parent element
        parent = self.find_element(self.PARENT_ELEMENT["locator"])
        # Find all <li> elements within the parent
        return parent.find_elements(By.TAG_NAME, self.ALL_ITEMS["locator"])

    def get_item_name_by_index(self, driver, ind):
        li_elements = self.get_list_of_all_items()
        item_name_element = li_elements[ind].find_element(
            By.XPATH, self.ITEM_NAME["locator"])
        # Get the text of the item name
        return item_name_element.text
