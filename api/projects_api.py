import requests
import allure


class ProjectsAPI:
    def __init__(self, base_url, token):
        self.project_id = None
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }

    @allure.step("Создать проект")
    def post_project(self, title):
        body = {"title": title}
        response = requests.post(
            f"{self.base_url}/api-v2/projects", json=body, headers=self.headers
        )
        if response.status_code == 201:
            self.project_id = response.json()["id"]
        return response

    @allure.step("Получить проект по ID")
    def get_project_by_id(self):
        response = requests.get(
            f"{self.base_url}/api-v2/projects/{self.project_id}",
            headers=self.headers,
        )
        return response

    @allure.step("Изменить название проекта")
    def update_project(self, title):
        body = {
            "title": title,
        }
        response = requests.put(
            f"{self.base_url}/api-v2/projects/{self.project_id}",
            json=body,
            headers=self.headers,
        )
        return response

    @allure.step("Отметить проект удаленным")
    def delete_project(self):
        body = {"deleted": True}
        response = requests.put(
            f"{self.base_url}/api-v2/projects/{self.project_id}",
            json=body,
            headers=self.headers,
        )
        return response

    @allure.step("Получить список проектов")
    def get_project(self):
        response = requests.get(
            f"{self.base_url}/api-v2/projects/", headers=self.headers
        )
        return response
