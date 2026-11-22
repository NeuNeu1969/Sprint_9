import allure

from pages.recipes_page import RecipesPage
from pages.signin_page import SigninPage


@allure.feature("Авторизация")
class TestSignin:

    @allure.title("После входа открывается главная страница")
    def test_signin_opens_main_page(self, driver, registered_user):
        recipes_page = RecipesPage(driver)
        recipes_page.open_main_page()
        recipes_page.click_signin_button()
        signin_page = SigninPage(driver)
        signin_page.fill_signin_form(registered_user["data"]["email"], registered_user["data"]["password"])
        signin_page.click_signin_form_button()

        assert recipes_page.is_recipes_page_opened()

    @allure.title("После входа в шапке отображается кнопка «Выход»")
    def test_signin_shows_logout_button(self, driver, registered_user):
        recipes_page = RecipesPage(driver)
        recipes_page.open_main_page()
        recipes_page.click_signin_button()
        signin_page = SigninPage(driver)
        signin_page.fill_signin_form(registered_user["data"]["email"], registered_user["data"]["password"])
        signin_page.click_signin_form_button()

        assert recipes_page.is_logout_button_displayed()
