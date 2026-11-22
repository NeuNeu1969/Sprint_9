from selenium.webdriver.common.by import By


class BasePageLocators:
    # Кнопки в шапке
    SIGNIN_BUTTON = (By.XPATH, "//header//a[text()='Войти']")
    SIGNUP_BUTTON = (By.XPATH, "//header//a[text()='Создать аккаунт']")
    LOGOUT_BUTTON = (By.XPATH, "//header//a[text()='Выход']")
    CREATE_RECIPE_TAB = (By.XPATH, "//header//a[text()='Создать рецепт']")
