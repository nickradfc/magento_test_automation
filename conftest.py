# In your conftest.py
from utilities.driver_manager import get_chrome_driver, get_firefox_driver

# Further down in the file where you set up the webdriver
def setup_method(self):
    self.driver = get_chrome_driver()  # or get_firefox_driver() depending on which one you want to use
