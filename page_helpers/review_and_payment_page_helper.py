from page_objects.review_and_payment_page import ReviewAndPaymentPage


def verify_billing_and_submit(driver):
    review_and_payment = ReviewAndPaymentPage(driver)
    review_and_payment.check_billing_checkbox_selected()
    review_and_payment.check_order_summary_info()
    review_and_payment.click_place_order()
