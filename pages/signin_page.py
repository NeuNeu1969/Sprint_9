import allure

from locators.signin_page_locators import SigninPageLocators
from pages.base_page import BasePage
from urls import SIGNIN_PAGE_URL


class SigninPage(BasePage):

    @allure.step("Открыть страницу входа")
    def open_signin_page(self):
        self.open(SIGNIN_PAGE_URL)

    def is_signin_page_opened(self):
        return self.wait_for_url(SIGNIN_PAGE_URL)

    def is_signin_form_displayed(self):
        return self.is_displayed(SigninPageLocators.SIGNIN_FORM)

    @allure.step("Заполнить форму входа")
    def fill_signin_form(self, email, password):
        self.set_text(SigninPageLocators.EMAIL_INPUT, email)
        self.set_text(SigninPageLocators.PASSWORD_INPUT, password)

    @allure.step("Нажать «Войти» под формой")
    def click_signin_form_button(self):
        self.click_element(SigninPageLocators.SIGNIN_BUTTON)
