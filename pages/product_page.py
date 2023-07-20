from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage
from locators.product_page_loc import PoductPageLocators


class ProductPage(BasePage):

    def should_be_product_name(self):
        product_title = self.is_element_present(*PoductPageLocators.PRODUCT_TITLE)
        assert product_title, "Product name is missing"
        return product_title.text

    def should_be_product_price(self):
        product_price = self.is_element_present(*PoductPageLocators.PRODUCT_PRICE)
        assert product_price, "Product price is missing"
        return product_price.text 

    def add_to_basket(self):
        button = self.is_element_present(*PoductPageLocators.ADD_TO_CART_BUTTON)
        assert button, "'Add to cart' button is missing"
        button.click()
        
    
    def handle_popup_form(self):
        print("handle")

    def check_product_name_in_success_message(self):
        return True

    def check_total_price_of_basket(self):
        return True

