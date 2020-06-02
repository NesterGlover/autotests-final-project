from pages.product_page import ProductPage
from selenium import webdriver


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
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


