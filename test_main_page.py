#Тесты с главной страницей сайта
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import allure

#Проверяем что переход по ссылке логина, ведет на корректную страницу с формами
def test_guest_should_see_login_page(browser):
    link="http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser,browser.current_url)
    login_page.should_be_login_page()

#Ожидаем, что есть текст о том что корзина пуста
#@pytest.mark.stepik
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,link)
    page.open()
    page.add_to_bascet_main()
    basket_page = BasketPage(browser,browser.current_url)
    basket_page.should_not_items()
    basket_page.should_not_items()

#@pytest.mark.login_guest

class TestLoginFromMainPage():
    # Проверка что ссылка логина есть на странице
    @allure.feature('guest_can_go_to_login_page')
    @allure.story('Проверка что ссылка логина есть на странице')
    def test_guest_can_go_to_login_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/"
        with allure.step("инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес"):
            page = MainPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        with allure.step("выполняем метод страницы — переходим на страницу логина"):
            page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина

    # Проверяем что можем перейти по ссылке логина
    def test_guest_should_see_login_link(self,browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()