import allure

from locators.signup_page_locators import SignupPageLocators
from pages.base_page import BasePage


class SignupPage(BasePage):

    @allure.step("Заполнить форму регистрации")
    def fill_signup_form(self, user_data):
        self.set_text(SignupPageLocators.FIRST_NAME_INPUT, user_data["first_name"])
        self.set_text(SignupPageLocators.LAST_NAME_INPUT, user_data["last_name"])
        self.set_text(SignupPageLocators.USERNAME_INPUT, user_data["username"])
        self.set_text(SignupPageLocators.EMAIL_INPUT, user_data["email"])
        self.set_text(SignupPageLocators.PASSWORD_INPUT, user_data["password"])

    @allure.step("Нажать «Создать аккаунт» под формой")
    def click_create_account_button(self):
        self.click_element(SignupPageLocators.CREATE_ACCOUNT_BUTTON)
