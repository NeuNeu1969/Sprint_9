import allure

from data import (
    RECIPE_INGREDIENT_QUERY,
    RECIPE_INGREDIENT_AMOUNT,
    RECIPE_COOKING_TIME,
    RECIPE_DESCRIPTION,
    RECIPE_IMAGE_PATH,
)
from helpers import generate_recipe_name
from pages.create_recipe_page import CreateRecipePage
from pages.recipe_page import RecipePage
from pages.recipes_page import RecipesPage


@allure.feature("Создание рецепта")
class TestCreateRecipe:

    def create_recipe(self, driver, name):
        # Заполнение всех полей формы и создание рецепта
        RecipesPage(driver).click_create_recipe_tab()
        create_recipe_page = CreateRecipePage(driver)
        create_recipe_page.set_name(name)
        create_recipe_page.add_ingredient(RECIPE_INGREDIENT_QUERY, RECIPE_INGREDIENT_AMOUNT)
        create_recipe_page.set_cooking_time(RECIPE_COOKING_TIME)
        create_recipe_page.set_description(RECIPE_DESCRIPTION)
        create_recipe_page.upload_image(RECIPE_IMAGE_PATH)
        create_recipe_page.click_create_recipe_button()

    @allure.title("После создания отображается карточка рецепта")
    def test_create_recipe_shows_recipe_card(self, logged_in_driver, created_recipes):
        self.create_recipe(logged_in_driver, generate_recipe_name())
        recipe_page = RecipePage(logged_in_driver)
        created_recipes.append(recipe_page.get_recipe_id())

        assert recipe_page.is_recipe_card_displayed()

    @allure.title("В карточке рецепта отображается название, введённое при создании")
    def test_create_recipe_shows_entered_name(self, logged_in_driver, created_recipes):
        name = generate_recipe_name()
        self.create_recipe(logged_in_driver, name)
        recipe_page = RecipePage(logged_in_driver)
        created_recipes.append(recipe_page.get_recipe_id())

        assert recipe_page.get_recipe_title() == name
