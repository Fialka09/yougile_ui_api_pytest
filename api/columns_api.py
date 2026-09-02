import requests
import allure


class ColumnsAPI:
    def __init__(self, base_url, token):
        self.board_id = None
        self.column_id = None
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }

    @allure.step(" Получить все колонки на доске")
    def get_columns(self):
        response = requests.get(
            f"{self.base_url}/api-v2/columns", headers=self.headers
        )
        return response

    @allure.step("Создать колонку")
    def post_new_columns(self, title, board_id):
        body = {"title": title, "boardId": board_id}
        response = requests.post(
            f"{self.base_url}/api-v2/columns", headers=self.headers, json=body
        )
        self.column_id = response.json()["id"]
        return response

    @allure.step("Получить колонку по ID")
    def get_column_id(self, column_id):
        response = requests.get(
            f"{self.base_url}/api-v2/columns/{column_id}", headers=self.headers
        )
        return response

    @allure.step("Изменить название колонки")
    def update_column_id(self, column_id, title):
        body = {"title": title}
        response = requests.put(
            f"{self.base_url}/api-v2/columns/{column_id}",
            headers=self.headers,
            json=body,
        )
        return response

    @allure.step("Отметить колонку удаленной")
    def delete_column_id(self, column_id):
        body = {"deleted": True}
        response = requests.put(
            f"{self.base_url}/api-v2/columns/{column_id}",
            headers=self.headers,
            json=body,
        )
        return response
