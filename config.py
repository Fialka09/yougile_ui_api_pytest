import os
import allure
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://ru.yougile.com"
LOGIN = os.getenv("YOUGILE_LOGIN")
PASSWORD = os.getenv("YOUGILE_PASSWORD")
COMPANY_ID = os.getenv("YOUGILE_COMPANY_ID")


@allure.step("Получить токен авторизации")
def get_token():
    """Получить токен: взять существующий или создать новый."""
    response = requests.post(
        f"{BASE_URL}/api-v2/auth/keys/get",
        json={"login": LOGIN, "password": PASSWORD, "companyId": COMPANY_ID},
    )
    keys = response.json()

    if len(keys) > 0:
        return keys[-1]["key"]

    response = requests.post(
        f"{BASE_URL}/api-v2/auth/keys",
        json={
            "login": LOGIN,
            "password": PASSWORD,
            "companyId": COMPANY_ID,
        },
    )
    if response.status_code != 201:
        raise Exception("Не удалось создать ключ")
    return response.json()["key"]
