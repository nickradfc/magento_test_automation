from page_objects.shopping_cart_page import ShoppingCartPage


def verify_page_title(driver):
    apparel_selection_page = ShoppingCartPage(driver)
    apparel_selection_page.assert_page_title()

def verify_cart_item_description(driver, specs):
    apparel_selection_page = ShoppingCartPage(driver)
    apparel_selection_page.verify_item_spec(specs["size"])
    apparel_selection_page.verify_item_spec(specs["color"])
    
def proceed_to_checkout(driver):
    apparel_selection_page = ShoppingCartPage(driver)
    apparel_selection_page.click_proceed_to_checkout()