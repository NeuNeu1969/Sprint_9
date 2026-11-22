from selenium.webdriver.common.by import By


class RecipePageLocators:
    RECIPE_CARD = (By.XPATH, "//div[contains(@class, 'styles_single-card__')]")
    RECIPE_TITLE = (By.XPATH, "//h1[contains(@class, 'styles_single-card__title')]")
