from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_backet_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_backet_button.click()


    def should_be_add_product_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
        "'Add to basket' button is not presented!"

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_H1_TAG), \
        "The product name is not presented!"

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_P_TAG), \
        "The product price is not presented!"

    def should_be_product_added_message(self, product_name):
        # сообщение имеет задержку, поэтому надо подождать его появления
        try:
            message_element = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(ProductPageLocators.ALERT_PRODUCT_NAME_STRONG_TAG)
            )
        except TimeoutException:
            message_element = None

        assert message_element != None, \
        "'The product has been added to basket' message is not presented!"


        product_name_in_message = \
            self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME_STRONG_TAG).text
        
        assert product_name == product_name_in_message, \
        "Product name on page is different from product name in alert message!"

    def should_be_product_price_message(self, product_price):
        # сообщение имеет задержку, поэтому надо подождать его появления
        try:
            message_element = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(ProductPageLocators.ALERT_PRODUCT_PRICE_STRONG_TAG)
            )
        except TimeoutException:
            message_element = None

        assert message_element != None, \
        "'Product price' message is not presented!" 


        product_price_in_message = \
            self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_PRICE_STRONG_TAG).text
        
        assert product_price == product_price_in_message, \
        "Product price on page is different from product price in alert message!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def is_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message did not disappear"


    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_H1_TAG).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_P_TAG).text

