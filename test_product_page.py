from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from selenium import webdriver
import pytest
import time


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

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)  # инициализация ProductPage
        page.open()                        # открытие страницы

        # проверяем, есть ли кнопка "добавить в корзину"
        page.should_be_add_product_to_basket_button() 
        page.should_be_product_name() # проверяем, если ли название у продукта
        page.should_be_product_price() # проверяем, есть ли цена у продукта

        page.add_product_to_basket() # добавляем продукт в корзину

        # проверяем, что есть сообщение о добавлении продукта в корзину и что название продукта
        # в сообщении совпадает с названием продукта на странице
        product_name_on_page = page.get_product_name() # получить название продукта на странице
        page.should_be_product_added_message(product_name_on_page) 

        # проверяем, что есть сообщение со стоимостью корзины и что стоимость корзины, указанная
        # в сообщении, совпадает со стоимолстью продукта на страницу
        product_price_on_page = page.get_product_price() # получить цену продукта на странице
        page.should_be_product_price_message(product_price_on_page) 
    

@pytest.mark.need_review
@pytest.mark.parametrize('link', [
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6',
    pytest.param('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7',
        marks=pytest.mark.xfail),
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9'
])
def test_guest_can_add_product_to_basket(browser, link):
    link = link
    page = ProductPage(browser, link)  # инициализация ProductPage
    page.open()                        # открытие страницы

    page.should_be_add_product_to_basket_button() # проверяем, есть ли кнопка "добавить в корзину"
    page.should_be_product_name() # проверяем, если ли название у продукта
    page.should_be_product_price() # проверяем, есть ли цена у продукта

    page.add_product_to_basket() # добавляем продукт в корзину
    page.solve_quiz_and_get_code() # решить задачу и получить код

    # проверяем, что есть сообщение о добавлении продукта в корзину и что название продукта
    # в сообщении совпадает с названием продукта на странице
    product_name_on_page = page.get_product_name() # получить название продукта на странице
    page.should_be_product_added_message(product_name_on_page) 

    # проверяем, что есть сообщение со стоимостью корзины и что стоимость корзины, указанная
    # в сообщении совпадает со стоимолстью продукта на страницу
    product_price_on_page = page.get_product_price() # получить цену продукта на странице
    page.should_be_product_price_message(product_price_on_page) 


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): # Fail
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)  # инициализация ProductPage
    page.open()                        # открытие страницы

    page.should_be_add_product_to_basket_button() # проверяем, есть ли кнопка "добавить в корзину"
    page.add_product_to_basket() # добавляем продукт в корзину

    page.should_not_be_success_message() # проверяем, что нет сообщения об успехе


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)  # инициализация ProductPage
    page.open()                        # открытие страницы

    page.should_not_be_success_message() # проверяем, что нет сообщения об успехе


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser): # Fail
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)  # инициализация ProductPage
    page.open()                        # открытие страницы

    page.should_be_add_product_to_basket_button() # проверяем, есть ли кнопка "добавить в корзину"
    page.add_product_to_basket() # добавляем продукт в корзину

    page.is_success_message_disappeared() # проверяем, что сообщение об успехе исчезло


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()

    page.should_be_basket_link()
    page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_basket_is_empty_text()