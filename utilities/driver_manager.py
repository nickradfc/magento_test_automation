from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def get_chrome_driver():
    return webdriver.Chrome(ChromeDriverManager().install())

def get_firefox_driver():
    return webdriver.Firefox(executable_path=GeckoDriverManager().install())
