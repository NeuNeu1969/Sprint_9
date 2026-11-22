from pathlib import Path

# Корень проекта
APP_DIR = Path(__file__).parent

# Фото для рецепта
RECIPE_IMAGE_PATH = str(APP_DIR / "assets" / "omelet.png")

# Данные пользователя, кроме почты и пароля
USER_FIRST_NAME = "Ivan"
USER_LAST_NAME = "Petrov"

# Данные рецепта
RECIPE_NAME_PREFIX = "Омлет"
RECIPE_INGREDIENT_QUERY = "яйц"
RECIPE_INGREDIENT_AMOUNT = "3"
RECIPE_COOKING_TIME = "15"
RECIPE_DESCRIPTION = "Взбить яйца с солью и пожарить на сковороде"
