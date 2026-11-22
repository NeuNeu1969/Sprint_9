# Sprint_9: UI-тесты «Продуктовый помощник»

Автотесты сервиса https://foodgram-frontend-1.foodgram.education-services.ru (Selenium + pytest + Allure).

## Покрытие

- Создание аккаунта
- Авторизация
- Создание рецепта (с загрузкой фото из `assets/`)

## Структура

- `pages/` Page Object, класс на страницу, общие методы и шапка в `base_page.py`
- `locators/` локаторы, файл на страницу
- `test/` тесты, класс на функциональность; фикстуры в `conftest.py`
- `data.py`, `urls.py`, `helpers.py` тестовые данные, адреса, подготовка данных через API
- `assets/` фото для рецепта
- `allure_results/` результаты для Allure-отчёта
- `Dockerfile`, `docker-compose.yml`, `browsers.json` запуск в Docker с Selenoid
- `.github/workflows/ci.yml` пайплайн GitHub Actions

## Запуск

Локально в Chrome:

```
pip install -r requirements.txt
pytest test --alluredir=allure_results
allure serve allure_results
```

В Docker с Selenoid:

```
docker pull selenoid/chrome:128.0
docker compose up --build --abort-on-container-exit --exit-code-from tests
```

## Особенности стенда

- При входе поле «Электронная почта» сверяется с username, поэтому в тестах username совпадает с почтой.
- Удалить пользователя через API нельзя. Созданные рецепты удаляются после теста.
