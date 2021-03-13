#методы для корзины внутри нее
from .base_page import BasePage
from .locators import ProductPageLocators

class BasketPage(BasePage):
    def should_not_items(self): # проверить что корзина пуста
        assert self.is_not_element_present(*ProductPageLocators.BASKET_ROW),"Items in Basket!!!"

    def should_message_in_basket(self): # проверить при пустой корзине сообщение
        assert  self.is_element_present(*ProductPageLocators.BASKET_MESSAGE), "NO MESSAGE BASKET INFO!!!"

