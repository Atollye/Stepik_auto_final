from pages.base_page import BasePage
from locators.main_page_loc import MainPageLocators

LINK_TO_PAGE = "http://selenium1py.pythonanywhere.com"


class MainPage(BasePage):

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), (
            "Login link is missing"
        )

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
