from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        self.guest_can_add_product()
        self.solve_quiz_and_get_code()
        self.message_basket_correct()

    def guest_can_add_product(self):
        self.browser.find_element(*ProductPageLocators.ADD_BASKET).click()

    def message_basket_correct(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_TEXT),"No success message"
        assert self.browser.find_element(*ProductPageLocators.BOOK_NAME).text  == self.browser.find_element(*ProductPageLocators.MESSAGE_TEXT).text, "The title of the book does not match the one added to the cart"
        assert self.is_element_present(*ProductPageLocators.INFO_TEXT), "No success message"
        assert self.browser.find_element(*ProductPageLocators.PRICE_TEXT).text in self.browser.find_element(*ProductPageLocators.INFO_TEXT).text, "The price of the book does not match the one added to the cart"
