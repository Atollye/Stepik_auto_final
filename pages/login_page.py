from pages.base_page import BasePage
from locators.login_page_loc import LoginPageLocators

LINK_TO_PAGE = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, (
            "Forwarding to login page doesn't work"
        )

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), (
            "No login form on login page"
        )

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), (
            "No register form on login page"
        )
