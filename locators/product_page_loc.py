from selenium.webdriver.common.by import By


class PoductPageLocators():
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCESS_NOTIFICATION = (
        By.CSS_SELECTOR, "#messages > :nth-child(1)  .alertinner"
    )
