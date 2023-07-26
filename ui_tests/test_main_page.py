import time

from selenium.webdriver.common.by import By

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage



MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com"


class TestTopPanel():

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, MAIN_PAGE_URL)
        page.open()
        page.should_be_link_to_basket()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_no_items_in_basket()
        basket_page.should_be_basket_emty_text()


    def test_guest_can_see_login_link(self, browser):
        page = MainPage(browser, MAIN_PAGE_URL)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, MAIN_PAGE_URL)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
