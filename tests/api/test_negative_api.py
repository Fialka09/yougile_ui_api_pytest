import allure
import requests
import pytest
from config import BASE_URL


@allure.feature("API")
@allure.story("Негативные тесты")
@allure.title("Создание проекта с невалидным названием")
@pytest.mark.api
@pytest.mark.negative
@pytest.mark.parametrize(
    "invalid_title",
    [
        "",
        " ",
        "   ",
    ],
)
def test_create_project_with_invalid_title(api, invalid_title):
    response = api.post_project(invalid_title)

    # Если проект создался (баг) — удаляем
    if response.status_code == 201:
        api.delete_project()

    assert response.status_code == 400


@allure.title("Получение несуществующего проекта")
@pytest.mark.api
@pytest.mark.negative
def test_get_nonexistent_project(token):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    response = requests.get(
        f"{BASE_URL}/api-v2/projects/00000000",
        headers=headers,
    )

    with allure.step("Проверить статус-код 404"):
        assert response.status_code == 404

    with allure.step("Проверить тело ошибки"):
        body = response.json()
        assert body["statusCode"] == 404
        assert body["message"] == "Проект не найден"


@allure.title("Запрос без токена")
@pytest.mark.api
@pytest.mark.negative
def test_request_without_token():
    response = requests.get(f"{BASE_URL}/api-v2/projects")

    with allure.step("Проверить статус-код 401"):
        assert response.status_code == 401

    with allure.step("Проверить тело ошибки"):
        body = response.json()
        assert body["statusCode"] == 401
        assert body["message"] == "Unauthorized"
