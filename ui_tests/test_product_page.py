import time

import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage

def get_urls():
    offers = []
    for offer_number in range(10):
        link = (
            f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        f"?promo=offer{offer_number}"
        )
        offers.append(link)
    return offers

class TestSpecialOffers():

    @pytest.mark.parametrize("offer", get_urls())
    def test_special_offers_guest_can_add_item_to_basket(self, browser, offer):
            page = ProductPage(browser, offer)
            page.open()
            product_name = page.should_be_product_name()
            product_price = page.should_be_product_price()
            page.add_to_basket()
            page.handle_allert()
            basket_page = BasketPage(browser, browser.current_url)
            time.sleep(10)
            basket_page.check_product_name_in_notification(product_name)
            basket_page.check_total_basket_price_in_notification(product_price)








