import allure
import requests
from config import BASE_URL


@allure.feature("API")
@allure.story("Негативные тесты")
@allure.title("Создание проекта с пустым названием")
def test_create_project_empty_title(token):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    response = requests.post(
        f"{BASE_URL}/api-v2/projects", json={"title": ""}, headers=headers
    )
    assert response.status_code == 400


@allure.title("Получение несуществующего проекта")
def test_get_nonexistent_project(token):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    response = requests.get(
        f"{BASE_URL}/api-v2/projects/00000000-0000-0000-0000-000000000000",
        headers=headers,
    )
    assert response.status_code == 404


@allure.title("Запрос без токена")
def test_request_without_token():
    response = requests.get(f"{BASE_URL}/api-v2/projects")
    assert response.status_code == 401
