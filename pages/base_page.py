from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from locators.locators import BasePageLocators

class BasePage():

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(5)

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_basket_page(self):
        login_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        login_link.click()

    def is_element_present(self, how, what):
        try:
            element = self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return element

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True
        return False

    def is_disappear(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.AUTHORIZED_USER_ICON),(
            "User is not authorized"
        )


    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), (
            "Login link is missing"
        )

    def should_be_link_to_basket(self):
        assert self.is_element_present(*BasePageLocators.BASKET_LINK), (
            "Basket page link is missing"
        )

