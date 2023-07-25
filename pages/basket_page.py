import time

from pages.base_page import BasePage
from locators.basket_page_loc import BasketPageLocators


class BasketPage(BasePage):

    def check_product_name_in_notification(self, product_name):
        success_notification = self.is_element_present(
            *BasketPageLocators.SUCCESS_NOTIFICATION
        )

        assert success_notification, (
            "No success notification after adding item to basket"
        )
        assert product_name in success_notification.text, (
            "No product name in success notification"
        )

    def check_total_basket_price_in_notification(self, product_price):
        price_in_notification = self.is_element_present(
            *BasketPageLocators.BASKET_PRICE_NOTIFICATION
        )
        assert price_in_notification, (
            "No price notification after adding item to basket"
        )
        assert product_price in price_in_notification.text, (
            "No product price in notification"
        )
    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *BasketPageLocators.SUCCESS_NOTIFICATION
        ), "There is a excessive success message"

    def success_message_should_disapear(self):
        notification = BasketPageLocators.SUCCESS_NOTIFICATION
        assert self.is_element_present(*notification), (
             "No success notification after adding item to basket"
        )
        assert self.is_disappear(*notification), (
            "Success message doesn't disappear"
        )
