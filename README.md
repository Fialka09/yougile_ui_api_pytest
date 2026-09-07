# YouGile UI и API автотесты
[Сайт YouGile](https://ru.yougile.com/)
## Описание проекта
Автоматизированное тестирование веб-приложения **YouGile** — системы управления проектами.

Тестирование охватывает:
- **API-тесты** — проверка работы с проектами, досками, колонками, задачами, пользователями
- **UI-тесты** — проверка авторизации, создания проектов, добавления задач

## Стек
- Python 3.14
- pytest
- Selenium
- Requests
- Allure
- python-dotenv

## Структура проекта
- `api/` — классы для работы с API
- `tests/api/` — API-тесты
- `tests/ui/` — UI-тесты
- `ui/pages/` — Page Objects
- `conftest.py` — фикстуры
- `config.py` — конфигурация
- `pytest.ini` — настройки pytest
- `requirements.txt` — зависимости
- `.env` — переменные окружения

## Установка
1. Склонировать проект:

```
git clone https://github.com/Fialka09/yougile_ui_api_pytest.git
```


2. Установить зависимости:

```pip install -r requirements.txt```

3. Создать файл .env с данными:
```
YOUGILE_LOGIN=ваш_email
YOUGILE_PASSWORD=ваш_пароль
YOUGILE_COMPANY_ID=id_компании
```

## Запуск тестов

### Все тесты:

`pytest`

#### Только API:

```pytest tests/api```

#### Только UI:

```pytest tests/ui```

#### С Allure-отчётом:

```pytest --alluredir=allure-results```
```allure generate allure-results -o allure-report```
```allure serve allure-results``` 

#### Повторный запуск упавших тестов

```pytest --reruns 2```

### Полезные ссылки


[Документация YouGile API v2.0](https://ru.yougile.com/api-v2#/)

[Документация Allure](https://allurereport.org/docs/)

