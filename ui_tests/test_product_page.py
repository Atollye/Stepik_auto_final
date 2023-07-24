import time

from pages.product_page import ProductPage
from pages.basket_page import BasketPage

PRODUCT_PAGE_URL = (
    'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-'
    'handbook_209/?promo=newYear'
)


class TestProductMainInfo():

    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, PRODUCT_PAGE_URL)
        page.open()
        product_name = page.should_be_product_name()
        product_price = page.should_be_product_price()
        page.add_to_basket()
        page.handle_allert()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.check_product_name_in_notification(product_name)
        basket_page.check_total_basket_price_in_notification(product_price)
