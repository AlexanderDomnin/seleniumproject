# методы для страницы логина
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self): # проверка корректных форм логина и юрла
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self,email,password): # регистрация
        self.browser.find_element(*LoginPageLocators.EMAIL_FORM).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FORM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD1_FORM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BTN_REGISTER).click()


    def should_be_login_url(self): # реализуйте проверку на корректный url адрес
        #self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        assert 'login' in self.browser.current_url,f"expected login to be substring of '{self.browser.current_url}'"

    def should_be_login_form(self): # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),"Login form is not presented"

    def should_be_register_form(self):# реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM),"Register form is not presented"