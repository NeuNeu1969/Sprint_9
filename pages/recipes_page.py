import allure

from pages.base_page import BasePage
from urls import BASE_URL, RECIPES_PAGE_URL


class RecipesPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open(BASE_URL)

    def is_recipes_page_opened(self):
        return self.wait_for_url(RECIPES_PAGE_URL)
