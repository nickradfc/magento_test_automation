from page_objects.single_apparel_page import SingleApparelPage


def verify_apparel_page_name(driver, name):
    apparel_page = SingleApparelPage(driver)
    apparel_page.assert_item_name(name)


def select_item_spec(driver, opt, opt_to_select):
    apparel_page = SingleApparelPage(driver)
    apparel_page.select_option(opt, opt_to_select)


def verify_spec_selected(driver, opt, opt_to_select):
    apparel_page = SingleApparelPage(driver)
    apparel_page.verify_option_selected(opt, opt_to_select)


def select_quantity(driver, qty):
    apparel_page = SingleApparelPage(driver)
    apparel_page.type_quantity(qty)


def verify_quantity_set(driver, qty):
    apparel_page = SingleApparelPage(driver)
    apparel_page.assert_qty(qty)


def add_to_cart(driver, qty):
    apparel_page = SingleApparelPage(driver)
    apparel_page.click_add_to_cart_btn()
    apparel_page.assert_cart_counter(qty)


def verify_item_added_banner(driver):
    apparel_page = SingleApparelPage(driver)
    apparel_page.item_added_success_banner()


def open_cart_from_banner(driver):
    apparel_page = SingleApparelPage(driver)
    apparel_page.click_banner_shpopping_cart()
