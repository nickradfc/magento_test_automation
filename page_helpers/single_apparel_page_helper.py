from page_objects.single_apparel_page import SingleApparelPage

def verify_apparel_page_name(driver, name):
    apparel_page = SingleApparelPage(driver)
    apparel_page.assert_item_name(name)