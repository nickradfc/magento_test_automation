from page_objects.my_account_helper import MyAccountPage


def verify_registration_banner(driver):
    my_account_page = MyAccountPage(driver)
    my_account_page.assert_successful_registration_banner()
