from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage
# from locators.product_page_loc import ProductPageLocators


class BasketPage(BasePage):

    def read_product_name_and_details():
        return ("Test product", "233")