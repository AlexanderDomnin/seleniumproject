from .base_page import BasePage
from .locators import ProductPageLocators

class BasketPage(BasePage):
    def should_not_items(self):
        assert self.is_not_element_present(*ProductPageLocators.BASKET_ROW),"Items in Basket!!!"

    def should_message_in_basket(self):
        assert  self.is_element_present(*ProductPageLocators.BASKET_MESSAGE), "NO MESSAGE BASKET INFO!!!"

