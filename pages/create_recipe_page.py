import allure

from locators.create_recipe_page_locators import CreateRecipePageLocators
from pages.base_page import BasePage


class CreateRecipePage(BasePage):

    @allure.step("Ввести название рецепта")
    def set_name(self, name):
        self.set_text(CreateRecipePageLocators.NAME_INPUT, name)

    @allure.step("Добавить ингредиент из списка")
    def add_ingredient(self, query, amount):
        # Список появляется, когда начинаешь вводить название
        self.set_text(CreateRecipePageLocators.INGREDIENT_INPUT, query)
        self.click_element(CreateRecipePageLocators.INGREDIENT_SUGGESTION)
        self.set_text(CreateRecipePageLocators.INGREDIENT_AMOUNT_INPUT, amount)
        self.click_element(CreateRecipePageLocators.ADD_INGREDIENT_BUTTON)
        self.find_element(CreateRecipePageLocators.ADDED_INGREDIENT)

    @allure.step("Ввести время приготовления")
    def set_cooking_time(self, minutes):
        self.set_text(CreateRecipePageLocators.COOKING_TIME_INPUT, minutes)

    @allure.step("Ввести описание")
    def set_description(self, description):
        self.set_text(CreateRecipePageLocators.DESCRIPTION_TEXTAREA, description)

    @allure.step("Загрузить фото")
    def upload_image(self, file_path):
        self.upload_file(CreateRecipePageLocators.IMAGE_INPUT, file_path)

    @allure.step("Нажать «Создать рецепт»")
    def click_create_recipe_button(self):
        self.click_element(CreateRecipePageLocators.CREATE_RECIPE_BUTTON)
