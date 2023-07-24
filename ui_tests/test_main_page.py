import time

from pages.main_page import MainPage
from pages.login_page import LoginPage

MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com"


class TestTopPanel():

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

    def test_login_page_is_ok(self, browser):
        page = LoginPage(browser)
        page.open()
        page.should_be_login_form()
        page.should_be_register_form()
        page.should_be_login_url
