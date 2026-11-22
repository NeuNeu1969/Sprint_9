from selenium.webdriver.common.by import By


class CreateRecipePageLocators:
    NAME_INPUT = (By.XPATH, "//div[text()='Название рецепта']/following-sibling::input")
    INGREDIENT_INPUT = (By.XPATH, "//input[contains(@class, 'styles_ingredientsInput')]")
    # Первый ингредиент в выпадающем списке
    INGREDIENT_SUGGESTION = (By.XPATH, "//div[contains(@class, 'styles_ingredientsInputs')]/div[contains(@class, 'styles_container')]/div[1]")
    INGREDIENT_AMOUNT_INPUT = (By.XPATH, "//input[contains(@class, 'styles_ingredientsAmountValue')]")
    ADD_INGREDIENT_BUTTON = (By.XPATH, "//div[text()='Добавить ингредиент']")
    ADDED_INGREDIENT = (By.XPATH, "//span[contains(@class, 'styles_ingredientsAddedItemTitle')]")
    COOKING_TIME_INPUT = (By.XPATH, "//div[text()='Время приготовления']/following-sibling::input")
    DESCRIPTION_TEXTAREA = (By.XPATH, "//div[text()='Описание рецепта']/following-sibling::textarea")
    IMAGE_INPUT = (By.XPATH, "//input[@type='file']")
    CREATE_RECIPE_BUTTON = (By.XPATH, "//button[text()='Создать рецепт']")
