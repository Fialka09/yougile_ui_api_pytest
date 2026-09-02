import allure
from config import BASE_URL
from api.projects_api import ProjectsAPI


@allure.feature("API")
@allure.story("Проекты")
@allure.title("Получение списка проектов")
def test_get_projects_list(token):
    api = ProjectsAPI(BASE_URL, token)
    response = api.get_project()
    assert response.status_code == 200


@allure.title("Получение проекта по ID")
def test_get_project_by_id(token):
    api = ProjectsAPI(BASE_URL, token)
    api.post_project("Проект для проверки")
    response = api.get_project_by_id()
    assert response.status_code == 200
    api.delete_project()
