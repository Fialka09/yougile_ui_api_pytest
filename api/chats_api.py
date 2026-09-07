import requests
import allure


class ChatsAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }

    @allure.step("Получить список чатов")
    def get_chats(self):
        response = requests.get(
            f"{self.base_url}/api-v2/group-chats",
            headers=self.headers,
        )
        return response

    @allure.step("Найти чат по названию")
    def find_chat_by_title(self, title):
        response = self.get_chats()
        chats = response.json().get("content", [])
        chat_title = f"Чат {title}"
        for chat in chats:
            if chat.get("title") == chat_title:
                return chat
        return None

    @allure.step("Удалить чат по ID")
    def delete_chat(self, chat_id):
        body = {"deleted": True}
        response = requests.put(
            f"{self.base_url}/api-v2/group-chats/{chat_id}",
            headers=self.headers,
            json=body,
        )
        return response

    @allure.step("Удалить чат по названию")
    def delete_chat_by_title(self, title):
        chat = self.find_chat_by_title(title)
        if chat:
            return self.delete_chat(chat["id"])
        return None
