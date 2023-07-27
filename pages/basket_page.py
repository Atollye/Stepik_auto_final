import time

from pages.base_page import BasePage
from locators.locators import BasketPageLocators

BASKET_PAGE_URL = "http://selenium1py.pythonanywhere.com/basket/"

class BasketPage(BasePage):

    def clear_basket(self):
        self.open()
        while True:
            items = self.browser.find_elements(*BasketPageLocators.BASKET_ITEM)
            if not items:
                break
            number = items[0].find_element(*BasketPageLocators.BASKET_ITEM_QUANTITY)
            number.clear()
            number.send_keys("0")
            update_btn = items[0].find_element(
                *BasketPageLocators.BASKET_ITEM_UPDATE_BUTTON
            )
            update_btn.click()
        self.should_be_basket_emty_text()


    def compare_product_name_in_notification(self, product_name):
        success_notification = self.is_element_present(
            *BasketPageLocators.SUCCESS_NOTIFICATION
        )

        assert success_notification, (
            "No success notification after adding item to basket"
        )
        assert product_name in success_notification.text, (
            "No product name in success notification"
        )

    def compare_basket_price_in_notification(self, product_price):
        price_in_notification = self.is_element_present(
            *BasketPageLocators.BASKET_PRICE_NOTIFICATION
        )
        assert price_in_notification, (
            "No price notification after adding item to basket"
        )
        assert product_price in price_in_notification.text, (
            "Incorrect price in notification"
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

    def should_be_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM
        ), "Basket is not empty as was expected"

    def should_be_items_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEM
        )

    def should_be_basket_emty_text(self):
        page_text = self.is_element_present(
            *BasketPageLocators.BASKET_EMPTY_TEXT
        )
        assert "Your basket is empty" in page_text.text, (
            "Wrong text on page when basket is empty"
        )
           