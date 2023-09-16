from page_objects.main_landing_page import MainLandingPage

def navigate_to_sign_in(driver):
    main_landing_page = MainLandingPage(driver)
    main_landing_page.navigate_to_sign_in()

def navigate_to_sign_up(driver):
    main_landing_page = MainLandingPage(driver)
    main_landing_page.navigate_to_sign_up()
