import time

import pytest

from pages.product_page import ProductPage
from pages.basket_page import BasketPage


sample_product_url = (
    "http://selenium1py.pythonanywhere.com/catalogue/reversing_202/"
)


class TestSpecialOffers():

    @pytest.mark.parametrize("offer", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    def test_special_offers_guest_can_add_item_to_basket(self, browser, offer):
        link = (
            f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work"
            f"_207/?promo=offer{offer}"
        )
        page = ProductPage(browser, link)
        page.open()
        product_name = page.should_be_product_name()
        product_price = page.should_be_product_price()
        page.add_to_basket()
        page.handle_allert()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.check_product_name_in_notification(product_name)
        basket_page.check_total_basket_price_in_notification(product_price)


class TestNoSuccessMessages():
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(
        self, browser
    ):
        page = ProductPage(browser, sample_product_url)
        page.open()
        page.add_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_success_message()

    def test_guest_can_not_see_success_message(self, browser):
        page = ProductPage(browser, sample_product_url)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, sample_product_url)
        page.open()
        page.add_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.success_message_should_disapear()
