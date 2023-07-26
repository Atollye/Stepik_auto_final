from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a")


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_EMAIL_FIELD = (By.NAME, "login-username")
    LOGIN_PASSWORD_FIELD = (By.NAME, "login-password")
    LOGIN_BUTTON = (By.NAME, "login-password")
    REGISTER_FORM = (By.ID, "register_form")


class PoductPageLocators():
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCESS_NOTIFICATION = (
        By.CSS_SELECTOR, "#messages > :nth-child(1)  .alertinner"
    )


class BasketPageLocators():
    SUCCESS_NOTIFICATION = (
        By.CSS_SELECTOR, "#messages > :nth-child(1)  .alertinner"
    )
    BASKET_PRICE_NOTIFICATION = (By.CSS_SELECTOR, ".alert-info p")
    BASKET_ITEM = (By.CLASS_NAME, "basket-items")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, ".content p")