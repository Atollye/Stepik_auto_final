import time

from selenium.webdriver.common.by import By

from pages.main_page import MainPage
from pages.login_page import LoginPage
from locators.main_page_loc import MainPageLocators

site_url = "http://selenium1py.pythonanywhere.com"


def test_guest_can_see_login_link(browser):
    page = MainPage(browser, site_url)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, site_url)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_login_page_is_ok(browser):
    page = LoginPage(browser)
    page.open()
    page.should_be_login_form()
    page.should_be_register_form()
    page.should_be_login_url


