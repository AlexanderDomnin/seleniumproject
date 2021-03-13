import pytest
from .pages.main_page import MainPage
from .pages.product_page import ProductPage

@pytest.mark.parametrize('part_link',["0","1","2","3","4","5","6",pytest.param("7", marks=pytest.mark.xfail),"8","9"])
def test_guest_can_add_product_to_basket_offer_numbers(part_link,browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{part_link}'
    page = MainPage(browser,link)
    page.open()
    product_page = ProductPage(browser,browser.current_url)
    product_page.guest_can_add_product_to_basket()

@pytest.mark.sm
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019.'
    page = MainPage(browser,link)
    page.open()
    product_page = ProductPage(browser,browser.current_url)
    product_page.guest_can_add_product_to_basket()

@pytest.mark.negative
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = MainPage(browser,link)
    page.open()
    guest_cant = ProductPage(browser,browser.current_url)
    guest_cant.guest_can_add_product()
    guest_cant.should_not_be_message()

@pytest.mark.negative
def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = MainPage(browser, link)
    page.open()
    guest_cant = ProductPage(browser, browser.current_url)
    guest_cant.should_not_be_message()

@pytest.mark.negative
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = MainPage(browser, link)
    page.open()
    guest_cant = ProductPage(browser, browser.current_url)
    guest_cant.guest_can_add_product()
    guest_cant.should_message_disappear()