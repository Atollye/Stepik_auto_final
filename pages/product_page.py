import math
import time

from pages.base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
from locators.product_page_loc import PoductPageLocators


class ProductPage(BasePage):

    def should_be_product_name(self):
        product_title = self.is_element_present(*PoductPageLocators.PRODUCT_TITLE)
        assert product_title, "Product title is missing"
        return product_title.text

    def should_be_product_price(self):
        product_price = self.is_element_present(*PoductPageLocators.PRODUCT_PRICE)
        assert product_price, "Product price is missing"
        return product_price.text

    def add_to_basket(self):
        button = self.is_element_present(*PoductPageLocators.ADD_TO_CART_BUTTON)
        assert button, "'Add to cart' button is missing"
        button.click()

    def handle_allert(self):
        alert = self.browser.switch_to.alert
        number = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(number))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            assert False, "There is no second alert"
