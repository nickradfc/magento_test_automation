from page_objects.home_page import HomePage

def open_my_account(driver):
    home_page = HomePage(driver)
    home_page.check_welcome_message()
    home_page.click_customer_menu_toggle()
    home_page.assert_my_account_btn_text()
    home_page.click_my_account_btn()


