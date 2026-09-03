import allure
from config import BASE_URL
from api.yougile_api import YougileAPI


@allure.feature("API")
@allure.story("Сквозной сценарий")
@allure.title("Пользователь → проект → доска → колонка → задача")
def test_scenario(token):
    api = YougileAPI(BASE_URL, token)

    api.get_users()
    api.post_project("Диплом-01", api.user_id)

    api.post_board("Моя доска", api.project_id)
    assert api.board_id is not None  # доска в API есть

    api.post_columns("Доделать", api.board_id)
    assert api.column_id is not None  # колонка в API есть

    api.post_task("Задача по диплому", api.column_id)
    assert api.task_id is not None  # задача в API есть
    api.put_task(api.task_id)
