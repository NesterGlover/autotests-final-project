from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a.btn")
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "div#content_inner > p")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")

    REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")

    PRODUCT_NAME_H1_TAG = (By.CSS_SELECTOR, "#content_inner .product_main h1")
    PRODUCT_PRICE_P_TAG = (By.CSS_SELECTOR, "#content_inner div.product_main .price_color")

    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]")

    ALERT_PRODUCT_NAME_STRONG_TAG = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
    ALERT_PRODUCT_PRICE_STRONG_TAG = (By.XPATH, "//div[@id='messages']/div[3]/div/p/strong")
    
