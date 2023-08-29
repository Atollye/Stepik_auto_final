import pytest

from pages.product_page import ProductPage
from pages.login_page import LoginPage, LOGIN_PAGE_URL
from pages.basket_page import BasketPage, BASKET_PAGE_URL


SAMPLE_PRODUCT_URL = (
    "http://selenium1py.pythonanywhere.com/catalogue/reversing_202/"
)


class TestGuestProductPageHeader():

    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, SAMPLE_PRODUCT_URL)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, SAMPLE_PRODUCT_URL)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(
        self, browser
    ):
        page = ProductPage(browser, SAMPLE_PRODUCT_URL)
        page.open()
        page.should_be_link_to_basket()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_no_items_in_basket()
        basket_page.should_be_basket_emty_text()


class TestUserCanAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, LOGIN_PAGE_URL)
        page.open()
        page.login_as_user()
        page.should_be_authorized_user()
        yield
        page = BasketPage(browser, BASKET_PAGE_URL)
        page.clear_basket()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, SAMPLE_PRODUCT_URL)
        page.open()
        expected_name = page.should_be_product_name()
        expected_price = page.should_be_product_price()
        page.add_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.compare_product_name_in_notification(expected_name)
        basket_page.compare_basket_price_in_notification(expected_price)

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, SAMPLE_PRODUCT_URL)
        page.open()
        page.should_not_be_success_message()


class TestSpecialOffers():
    
    @pytest.mark.need_review
    @pytest.mark.parametrize("offer", [0, 1, 2])
    def test_guest_can_add_product_to_basket(self, browser, offer):
        link = (
            f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work"
            f"_207/?promo=offer{offer}"
        )
        page = ProductPage(browser, link)
        page.open()
        expected_name = page.should_be_product_name()
        expected_price = page.should_be_product_price()
        page.add_to_basket()
        page.handle_allert()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.compare_product_name_in_notification(expected_name)
        basket_page.compare_basket_price_in_notification(expected_price)


class TestNoSuccessMessages():
    @pytest.mark.xfail
    def test_guest_can_not_see_success_message_after_adding_product_to_basket(
        self, browser
    ):
        page = ProductPage(browser, SAMPLE_PRODUCT_URL)
        page.open()
        page.add_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, SAMPLE_PRODUCT_URL)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, SAMPLE_PRODUCT_URL)
        page.open()
        page.add_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.success_message_should_disapear()
