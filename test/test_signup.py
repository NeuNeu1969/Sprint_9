import allure

from pages.recipes_page import RecipesPage
from pages.signin_page import SigninPage
from pages.signup_page import SignupPage


@allure.feature("Создание аккаунта")
class TestSignup:

    @allure.title("После регистрации открывается страница авторизации")
    def test_signup_opens_signin_page(self, driver, user_data):
        recipes_page = RecipesPage(driver)
        recipes_page.open_main_page()
        recipes_page.click_signup_button()
        signup_page = SignupPage(driver)
        signup_page.fill_signup_form(user_data)
        signup_page.click_create_account_button()

        assert SigninPage(driver).is_signin_page_opened()

    @allure.title("После регистрации отображается форма авторизации")
    def test_signup_shows_signin_form(self, driver, user_data):
        recipes_page = RecipesPage(driver)
        recipes_page.open_main_page()
        recipes_page.click_signup_button()
        signup_page = SignupPage(driver)
        signup_page.fill_signup_form(user_data)
        signup_page.click_create_account_button()

        assert SigninPage(driver).is_signin_form_displayed()
