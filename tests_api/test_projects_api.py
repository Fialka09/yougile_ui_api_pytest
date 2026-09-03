import allure


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
