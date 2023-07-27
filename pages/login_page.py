
from pages.base_page import BasePage
from locators.locators import LoginPageLocators

LOGIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/accounts/login/"


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

    def login_as_user(self):
        email_field = self.is_element_present(
            *LoginPageLocators.LOGIN_EMAIL_FIELD
        )
        assert email_field, "No email field on login page"
        email_field.send_keys("user@user.com")

        password_field = self.is_element_present(
            *LoginPageLocators.LOGIN_PASSWORD_FIELD
        )
        assert password_field, "No password field on login page"
        password_field.send_keys("testpassword")

        login_button = self.is_element_present(*LoginPageLocators.LOGIN_BUTTON)
        assert login_button, "No login_button on login page"
        login_button.click()
