from selenium.webdriver.common.by import By


class BasketPageLocators():
    SUCCESS_NOTIFICATION = (
        By.CSS_SELECTOR, "#messages > :nth-child(1)  .alertinner"
    )
    BASKET_PRICE_NOTIFICATION = (By.CSS_SELECTOR, ".alert-info p")
