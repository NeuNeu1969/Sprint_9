from locators.recipe_page_locators import RecipePageLocators
from pages.base_page import BasePage
from urls import CREATE_RECIPE_PAGE_URL


class RecipePage(BasePage):

    def get_recipe_id(self):
        # После создания адрес меняется на /recipes/68
        url = self.wait_for_url_change(CREATE_RECIPE_PAGE_URL)
        return url.split("/")[-1]

    def is_recipe_card_displayed(self):
        return self.is_displayed(RecipePageLocators.RECIPE_CARD)

    def get_recipe_title(self):
        return self.get_text(RecipePageLocators.RECIPE_TITLE)
