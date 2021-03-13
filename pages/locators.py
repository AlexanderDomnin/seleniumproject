from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") # форма логина
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form") # форма регистрации

class ProductPageLocators():
    ADD_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form") # добавить в корзину на странице товара
    MESSAGE_TEXT = (By.XPATH,"//*[@id='messages']/div[1]/div/strong") # текст о успешном добавлении в корзину
    BOOK_NAME = (By.XPATH, "//div[contains(@class,'product_main')]/h1") # название книги
    INFO_TEXT = (By.XPATH, "//*[@id='messages']/div[contains(@class,'alert-info')]") # текст о цене
    PRICE_TEXT = (By.XPATH, "//div[contains(@class,'product_main')]/p[contains(@class,'price_color')]") # цена товара
    MESSAGE_BOX = (By.XPATH,"//*[@id='messages'']/div[1]") # текст с успешным уведомлением
    BASKET_ROW = (By.XPATH,"//*[@class='basket-items'][1]") # ряд с выбранными книгами в корзине
    BASKET_MESSAGE = (By.XPATH,"//*[@id='content_inner']/p[normalize-space(text())='Ваша корзина пуста' or normalize-space(text())='Your basket is empty.']") # сообщение если корзина пуста


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") # ссылка на логин
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR,"#login_linc_inc") # ссылка на не валидный логин
    BASKET_LINK = (By.XPATH,"//a[@class='btn btn-default']") #ссылка на вход в корзину с любой страницы