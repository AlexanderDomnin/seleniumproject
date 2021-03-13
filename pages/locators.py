from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form")
    MESSAGE_TEXT = (By.XPATH,"//*[@id='messages']/div[1]/div/strong")
    BOOK_NAME = (By.XPATH, "//div[contains(@class,'product_main')]/h1")
    INFO_TEXT = (By.XPATH, "//*[@id='messages']/div[contains(@class,'alert-info')]")
    PRICE_TEXT = (By.XPATH, "//div[contains(@class,'product_main')]/p[contains(@class,'price_color')]")