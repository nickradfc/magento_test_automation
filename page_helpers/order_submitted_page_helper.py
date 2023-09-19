from page_objects.order_submitted_page import OrderSubmittedPage


def verify_order_placed(driver):
    order_submitted_page = OrderSubmittedPage(driver)
    order_submitted_page.check_order_confirmation_title()
    order_submitted_page.check_order_number()
