from selenium.webdriver.common.by import By


class BasketPageLocators():
    SUCCESS_NOTIFICATION = (By.CSS_SELECTOR, ".alert-success .alertinner")
    BASKET_PRICE_NOTIFICATION = (By.CSS_SELECTOR, ".alert-info p")
