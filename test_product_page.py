from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from selenium import webdriver
import pytest
import time


@pytest.mark.product_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()

        page.should_be_login_page()
        
        email = str(time.time()) + "@fakemail.org"
        password = "testpassword12"
        page.register_new_user(email, password)

        page.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)  # инициализация ProductPage
        page.open()                        # открытие страницы

        page.should_not_be_success_message() # проверяем, что нет сообщения об успехе

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)  # инициализация ProductPage
        page.open()                        # открытие страницы

        page.should_be_add_product_to_basket_button() # проверяем, есть ли кнопка "добавить в корзину"
        page.should_be_product_name() # проверяем, если ли название у продукта
        page.should_be_product_price() # проверяем, есть ли цена у продукта


        page.add_product_to_basket() # добавляем продукт в корзину
        # page.solve_quiz_and_get_code() 


        page.should_be_product_added_message() # проверяем, что есть сообщение о том, что продукт добавлен в корзину
        product_name_on_page = page.get_product_name() # получить название продукта на странице
        product_name_in_message = page.get_product_name_from_alert_message() # получить название продукта из сообщения
        assert product_name_on_page == product_name_in_message, "Product name on page is different from product name in alert message!"


        page.should_be_product_price_message() # проверяем, что есть сообщение со стоимостью корзины
        product_price_on_page= page.get_product_price() # получить цену продукта на странице
        product_price_in_message = page.get_product_price_from_alert_message() # получить цену продукта из сообщения
        assert product_price_on_page == product_price_in_message, "Product price on page is different from product price in alert message!"
    

@pytest.mark.skip(reason="testing other cases")
@pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6',
                                  pytest.param('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7', marks=pytest.mark.xfail),
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9'])
def test_guest_can_add_product_to_basket(browser, link):
    link = link
    page = ProductPage(browser, link)  # инициализация ProductPage
    page.open()                        # открытие страницы

    page.should_be_add_product_to_basket_button() # проверяем, есть ли кнопка "добавить в корзину"
    page.should_be_product_name() # проверяем, если ли название у продукта
    page.should_be_product_price() # проверяем, есть ли цена у продукта


    page.add_product_to_basket() # добавляем продукт в корзину
    page.solve_quiz_and_get_code() # решить задачу и получить код


    page.should_be_product_added_message() # проверяем, что есть сообщение о том, что продукт добавлен в корзину
    product_name_on_page = page.get_product_name() # получить название продукта на странице
    product_name_in_message = page.get_product_name_from_alert_message() # получить название продукта из сообщения
    assert product_name_on_page == product_name_in_message, "Product name on page is different from product name in alert message!"


    page.should_be_product_price_message() # проверяем, что есть сообщение со стоимостью корзины
    product_price_on_page= page.get_product_price() # получить цену продукта на странице
    product_price_in_message = page.get_product_price_from_alert_message() # получить цену продукта из сообщения
    assert product_price_on_page == product_price_in_message, "Product price on page is different from product price in alert message!"


@pytest.mark.skip(reason="testing other cases")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)  # инициализация ProductPage
    page.open()                        # открытие страницы

    page.should_be_add_product_to_basket_button() # проверяем, есть ли кнопка "добавить в корзину"
    page.add_product_to_basket() # добавляем продукт в корзину

    page.should_not_be_success_message() # проверяем, что нет сообщения об успехе


@pytest.mark.skip(reason="testing other cases")
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)  # инициализация ProductPage
    page.open()                        # открытие страницы

    page.should_not_be_success_message() # проверяем, что нет сообщения об успехе


@pytest.mark.skip(reason="testing other cases")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)  # инициализация ProductPage
    page.open()                        # открытие страницы

    page.should_be_add_product_to_basket_button() # проверяем, есть ли кнопка "добавить в корзину"
    page.add_product_to_basket() # добавляем продукт в корзину

    page.is_success_message_disappeared() # проверяем, что сообщение об успехе исчезло


@pytest.mark.skip(reason="testing other cases")
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.skip(reason="testing other cases")
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()

    page.should_be_basket_link()
    page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_basket_is_empty_text()