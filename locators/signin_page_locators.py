from selenium.webdriver.common.by import By


class SigninPageLocators:
    SIGNIN_FORM = (By.XPATH, "//h1[text()='Войти на сайт']/following-sibling::form")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SIGNIN_BUTTON = (By.XPATH, "//form//button[text()='Войти']")
