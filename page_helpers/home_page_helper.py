from page_objects.home_page import HomePage

def open_my_account(driver):
    home_page = HomePage(driver)
    home_page.check_welcome_message()
    home_page.click_customer_menu_toggle()
    home_page.assert_my_account_btn_text()
    home_page.click_my_account_btn()

def verify_welcome_message(driver):
    home_page = HomePage(driver)
    home_page.check_welcome_message()

def select_main_category(driver, category):
    home_page = HomePage(driver)
    category_map = {
        "Women": home_page.select_women_category,
        # "Men": home_page.select_men_category,
    }
    category_map[category]()
    home_page.assert_category_page_title(category)

def select_apparel(driver, apparely_category):
    home_page = HomePage(driver)
    category_map = {
        "Jackets": home_page.select_jacket_category,
    }
    category_map[apparely_category]()
    home_page.assert_apparel_category_page_title(apparely_category)



