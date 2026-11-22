import pytest
from selenium import webdriver

from helpers import generate_user_data, register_user, delete_recipe
from pages.recipes_page import RecipesPage
from pages.signin_page import SigninPage


def pytest_addoption(parser):
    # Адрес Selenoid, например http://selenoid:4444/wd/hub; без него тесты идут в локальном Chrome
    parser.addoption("--selenoid-uri", action="store", default=None)


@pytest.fixture
def driver(request):
    selenoid_uri = request.config.getoption("--selenoid-uri")
    if selenoid_uri:
        browser = webdriver.Remote(command_executor=selenoid_uri, options=webdriver.ChromeOptions())
    else:
        browser = webdriver.Chrome()
    browser.set_window_size(1920, 1080)
    yield browser
    browser.quit()


@pytest.fixture
def user_data():
    # Данные для регистрации через форму
    return generate_user_data()


@pytest.fixture
def registered_user():
    # Пользователь создаётся через API, удалить его стенд не даёт
    data = generate_user_data()
    token = register_user(data)
    return {"data": data, "token": token}


@pytest.fixture
def logged_in_driver(driver, registered_user):
    signin_page = SigninPage(driver)
    signin_page.open_signin_page()
    signin_page.fill_signin_form(registered_user["data"]["email"], registered_user["data"]["password"])
    signin_page.click_signin_form_button()
    RecipesPage(driver).is_recipes_page_opened()
    return driver


@pytest.fixture
def created_recipes(registered_user):
    # Id рецептов, созданных в тесте; после теста удаляются через API
    recipe_ids = []
    yield recipe_ids
    for recipe_id in recipe_ids:
        delete_recipe(recipe_id, registered_user["token"])
