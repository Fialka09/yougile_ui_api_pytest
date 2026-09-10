import allure
import pytest


@allure.feature("API")
@allure.story("Проекты")
@allure.title("Создание проекта")
def test_create_project(api):
    response = api.post_project("Диплом")
    assert response.status_code == 201
    api.delete_project()


@allure.title("Обновление проекта")
def test_update_project(api):
    api.post_project("Диплом")
    response = api.update_project("Диплом сдан")
    assert response.status_code == 200

    check = api.get_project_by_id()
    assert check.json()["title"] == "Диплом сдан"

    api.delete_project()


@allure.title("Отметить проект удалённым")
def test_delete_project(api):
    api.post_project("Отметить удаленным")
    response = api.delete_project()

    assert response.status_code == 200

    check = api.get_project_by_id()
    assert check.json()["deleted"] is True


@allure.title("Создание проекта с разными названиями")
@pytest.mark.api
@pytest.mark.parametrize(
    "project_title",
    [
        "Диплом2026",
        "Проект на русском",
        "Diploma Project",
        "12345",
        "Проект-тест_1",
    ],
)
def test_create_project_with_different_titles(api, project_title):
    response = api.post_project(project_title)
    assert response.status_code == 201
    api.delete_project()
