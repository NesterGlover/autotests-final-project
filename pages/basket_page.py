from .base_page import BasePage
from .locators import BasePageLocators
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_ITEMS), \
        "Basket items are present, but should not be!"

    def should_be_basket_is_empty_text(self):
        assert self.is_element_present(*BasePageLocators.BASKET_EMPTY_TEXT), \
        "Basket is empty text is not presented!"