import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def set_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    def upload_file(self, locator, file_path):
        # Поле input[type=file] скрыто, поэтому ждём его наличия, а не видимости
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)).send_keys(file_path)

    def get_text(self, locator):
        return self.find_element(locator).text

    def is_displayed(self, locator):
        return self.find_element(locator).is_displayed()

    def wait_for_url(self, url):
        return WebDriverWait(self.driver, 10).until(EC.url_to_be(url))

    def wait_for_url_change(self, old_url):
        WebDriverWait(self.driver, 10).until(EC.url_changes(old_url))
        return self.driver.current_url

    @allure.step("Нажать «Войти» в шапке")
    def click_signin_button(self):
        self.click_element(BasePageLocators.SIGNIN_BUTTON)

    @allure.step("Нажать «Создать аккаунт» в шапке")
    def click_signup_button(self):
        self.click_element(BasePageLocators.SIGNUP_BUTTON)

    @allure.step("Перейти на таб «Создать рецепт»")
    def click_create_recipe_tab(self):
        self.click_element(BasePageLocators.CREATE_RECIPE_TAB)

    def is_logout_button_displayed(self):
        return self.is_displayed(BasePageLocators.LOGOUT_BUTTON)
