from page_objects.apparel_selection_page import ApparelSelectionPage

def select_item_by_index(driver, ind):
    apparel_selection_page = ApparelSelectionPage(driver)
    apparel_selection_page.select_item_by_index(driver, ind)

def get_apparel_name_by_index(driver, ind):
    apparel_selection_page = ApparelSelectionPage(driver)
    return apparel_selection_page.get_item_name_by_index(driver, ind)