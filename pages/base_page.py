#основные методы, которые могут быть использованы везде
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import math

class BasePage():
    def __init__(self,browser,url,timeout=5): #инициализация конструктора
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def add_to_bascet_main(self): # Добавить в корзину
        self.browser.find_element(*BasePageLocators.BASKET_LINK).click()

    def go_to_login_page(self): # Кликнуть на вход или регистрацию
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()

    def is_disappeared(self, how, what, timeout=4): # ПРоверить что элемент исчез через заданное время
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_element_present(self, how, what): # проверить что элемент есть на сайте
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self,how,what,timeout=4):# проверить что элемента нет есть на сайте
        try:
            WebDriverWait(self.browser,timeout).until(EC.presence_of_element_located((how,what)))
        except TimeoutException:
            return True
        return False

    def open(self): # открыть сайт
        self.browser.get(self.url)

    def should_be_login_link(self): # проверить что ссылка есть на сайте
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self): # проверить что пользователь залогинен
        assert self.is_element_present(*BasePageLocators.USER_ICON),"User icon is not presented,robably unauthorised user"

    def solve_quiz_and_get_code(self): # степик квиз
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")