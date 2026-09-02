import requests
import uuid
import allure


class YougileAPI:

    def __init__(self, base_url, token):
        self.idempotency_key = None
        self.project_id = None
        self.board_id = None
        self.column_id = None
        self.task_id = None
        self.user_id = None
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

    @allure.step("Получить список проектов")
    def get_projects(self):
        return requests.get(
            f"{self.base_url}/api-v2/projects", headers=self.headers
        )

    @allure.step("Получить данные о текущем пользователе")
    def get_users(self):
        response = requests.get(
            f"{self.base_url}/api-v2/users/me", headers=self.headers
        )
        self.user_id = response.json()["id"]
        return response

    def post_project(self, title, user_id):
        self.idempotency_key = str(uuid.uuid4())
        body = {
            "title": title,
            "users": {user_id: "admin"},
            "idempotencyKey": self.idempotency_key,
        }
        response = requests.post(
            f"{self.base_url}/api-v2/projects", json=body, headers=self.headers
        )
        self.project_id = response.json()["id"]
        return response

    @allure.step("Создать доску в проекте")
    def post_board(self, title, project_id):
        body = {"title": title, "projectId": project_id}
        response = requests.post(
            f"{self.base_url}/api-v2/boards", json=body, headers=self.headers
        )
        self.board_id = response.json()["id"]
        return response

    @allure.step("Создать колонку на доске")
    def post_collumns(self, title, board_id):
        body = {
            "title": title,
            "boardId": board_id,
        }
        response = requests.post(
            f"{self.base_url}/api-v2/columns", json=body, headers=self.headers
        )
        self.column_id = response.json()["id"]
        return response

    @allure.step("Создать задачу с дедлайном 15.09.2026")
    def post_task(
        self,
        title,
        column_id,
    ):
        body = {
            "title": title,
            "columnId": column_id,
            "deadline": {
                "deadline": 1787356800000,
                "startDate": 1787356800000,
                "withTime": False,
            },
        }
        response = requests.post(
            f"{self.base_url}/api-v2/tasks", json=body, headers=self.headers
        )
        self.task_id = response.json()["id"]
        return response

    @allure.step("Отметить задачу выполненной")
    def put_task(self, task_id):
        self.task_id = task_id
        body = {"completed": True}
        return requests.put(
            f"{self.base_url}/api-v2/tasks/{task_id}",
            json=body,
            headers=self.headers,
        )

    @allure.step("Повторить создание проекта с тем же ключом")
    def post_project_idempotent(self, title, user_id):
        body = {
            "title": title,
            "users": {user_id: "admin"},
            "idempotencyKey": self.idempotency_key  # тот же ключ
        }
        response = requests.post(
            f"{self.base_url}/api-v2/projects",
            json=body,
            headers=self.headers
        )
        return response

