import random
import string

import requests

from data import USER_FIRST_NAME, USER_LAST_NAME, RECIPE_NAME_PREFIX
from urls import USERS_ENDPOINT, LOGIN_ENDPOINT, RECIPES_ENDPOINT


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_user_data():
    # Стенд ищет пользователя при входе по username, поэтому username совпадает с почтой
    email = generate_random_string(10) + "@yandex.ru"
    return {
        "first_name": USER_FIRST_NAME,
        "last_name": USER_LAST_NAME,
        "username": email,
        "email": email,
        "password": generate_random_string(10),
    }


def generate_recipe_name():
    return RECIPE_NAME_PREFIX + " " + generate_random_string(5)


def register_user(user_data):
    # Регистрация через API и получение токена
    requests.post(USERS_ENDPOINT, json=user_data)
    response = requests.post(LOGIN_ENDPOINT, json={"email": user_data["email"], "password": user_data["password"]})
    return response.json()["auth_token"]


def delete_recipe(recipe_id, token):
    requests.delete(RECIPES_ENDPOINT + recipe_id + "/", headers={"Authorization": "Token " + token})
