import requests
import allure


class BoardsAPI:

    def __init__(self, base_url, token):
        self.project_id = None
        self.board_id = None
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }

    @allure.step("Получить все доски")
    def get_all_boards(self):
        response = requests.get(
            f"{self.base_url}/api-v2/boards", headers=self.headers
        )
        return response

    @allure.step("Создать доску")
    def post_new_board(self, project_id, title):
        body = {"title": title, "projectId": project_id}
        response = requests.post(
            f"{self.base_url}/api-v2/boards", headers=self.headers, json=body
        )
        self.board_id = response.json()["id"]
        return response

    @allure.step("Получить доску по ID")
    def get_board_by_id(self, board_id):
        response = requests.get(
            f"{self.base_url}/api-v2/boards/{board_id}", headers=self.headers
        )
        return response

    @allure.step("Отметить доску удаленной")
    def delete_board_by_id(self, board_id):
        body = {
            "deleted": True,
        }
        response = requests.put(
            f"{self.base_url}/api-v2/boards/{board_id}",
            json=body,
            headers=self.headers,
        )
        return response

    @allure.step("Изменить название доски")
    def update_board_by_id(self, board_id, title):
        body = {"title": title}
        response = requests.put(
            f"{self.base_url}/api-v2/boards/{board_id}",
            json=body,
            headers=self.headers,
        )
        return response
