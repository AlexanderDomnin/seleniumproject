#Тесты с страницей товара в корзине
import pytest
import time
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

#Проверяем на 10 разных страницах, упадет тест или нет
@pytest.mark.parametrize('part_link',["0","1","2","3","4","5","6",pytest.param("7", marks=pytest.mark.xfail),"8","9"])
def test_guest_can_add_product_to_basket_offer_numbers(part_link,browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{part_link}'
    page = MainPage(browser,link)
    page.open()
    product_page = ProductPage(browser,browser.current_url)
    product_page.guest_can_add_product_to_basket()

#Проверка добавления в корзину, должны быть сообщения об удачной корзине и название с ценой совпадают, с добавленными
@pytest.mark.sm
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019.'
    page = MainPage(browser,link)
    page.open()
    product_page = ProductPage(browser,browser.current_url)
    product_page.guest_can_add_product_to_basket()

#Проверка, что на странице, нет сообщения о удачном добавлении в корзину
@pytest.mark.negative
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = MainPage(browser,link)
    page.open()
    guest_cant = ProductPage(browser,browser.current_url)
    guest_cant.guest_can_add_product()
    guest_cant.should_not_be_message()

#Проверка, что на странице, нет сообщения о удачном добавлении в корзину, без добавления в корзину
@pytest.mark.negative #маркировка для негативных тестов
def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = MainPage(browser, link)
    page.open()
    guest_cant = ProductPage(browser, browser.current_url)
    guest_cant.should_not_be_message()

#Проверка, что на странице, нет сообщения о удачном добавлении в корзину, с другим методом(ожидаем чт ов течении 4 секунд элемента не будет)
@pytest.mark.negative
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = MainPage(browser, link)
    page.open()
    guest_cant = ProductPage(browser, browser.current_url)
    guest_cant.guest_can_add_product()
    guest_cant.should_message_disappear()

#Проверка что ссылка логина есть на странице
@pytest.mark.sm
def test_guest_should_see_login_link_on_product_page(browser):
    link='http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser,link)
    page.open()
    page.should_be_login_link()

#Проверяем что можем перейти по ссылке логина
@pytest.mark.sm
def test_guest_can_go_to_login_page_from_product_page(browser):
    link='http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser,link)
    page.open()
    page.go_to_login_page()

#Ожидаем, что есть текст о том что корзина пуста
@pytest.mark.stepik
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = MainPage(browser, link)
    page.open()
    page.add_to_bascet_main()
    basket_page = BasketPage(browser,browser.current_url)
    basket_page.should_not_items()
    basket_page.should_message_in_basket()

@pytest.mark.stepi
class TestUserAddToBasketFromProductPage:
    #сетап
    @pytest.fixture(scope="function",autouse=True)
    def setup(self,browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.register_new_user(email=email, password=password)
        self.page.should_be_authorized_user()

    # Проверка, что на странице, нет сообщения о удачном добавлении в корзину, без добавления в корзину
    def test_user_cant_see_success_message(self,browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = MainPage(browser, link)
        page.open()
        guest_cant = ProductPage(browser, browser.current_url)
        guest_cant.should_not_be_message()

    # Проверка добавления в корзину, должны быть сообщения об удачной корзине и название с ценой совпадают, с добавленными
    def test_user_can_add_product_to_basket(self,browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = MainPage(browser, link)
        page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.guest_can_add_product_to_basket()

