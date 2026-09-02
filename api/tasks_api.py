import requests
import allure

class TasksAPI:
    def __init__(self, base_url, token):
        self.column_id = None
        self.task_id = None
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }

    @allure.step("Получить список задач")
    def get_tasks(self):
        response = requests.get(f"{self.base_url}/api-v2/task-list", headers=self.headers)
        return response

    @allure.step("Создать задачу")
    def post_task(self, title, column_id):
        body = {
            "title": title,
            "columnId": column_id,
        }
        response = requests.post(f"{self.base_url}/api-v2/tasks",
                                json=body, headers=self.headers)
        self.task_id = response.json()["id"]
        return response


    @allure.step("Получить задачу по ID")
    def get_task_by_id(self, task_id):
        response = requests.get(f"{self.base_url}/api-v2/tasks/{task_id}",
                                headers=self.headers)
        return response

    @allure.step("Отметить выполненной")
    def complete_task(self, task_id):
        body = {"completed": True,}
        response = requests.put(f"{self.base_url}/api-v2/tasks/{task_id}", json=body,
                                   headers=self.headers)
        return response

    @allure.step("Архивировать")
    def archive_task(self, task_id):
        body = {"archived": True}
        response = requests.put(f"{self.base_url}/api-v2/tasks/{task_id}", json=body,
                                headers=self.headers)
        return response
