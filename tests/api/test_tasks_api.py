import allure
import pytest


@allure.feature("API")
@allure.story("Задачи")
@allure.title("Создание задачи")
@pytest.mark.api
@pytest.mark.positive
def test_create_task(api, boards_api, columns_api, tasks_api):
    api.post_project("Проект для задачи")
    boards_api.post_new_board(api.project_id, "Доска")
    columns_api.post_new_columns("To do", boards_api.board_id)

    response = tasks_api.post_task("Задача по диплому", columns_api.column_id)

    assert response.status_code == 201
    assert tasks_api.task_id is not None

    api.delete_project()


@allure.title("Отметить задачу выполненной")
@pytest.mark.api
@pytest.mark.positive
def test_update_task(api, boards_api, columns_api, tasks_api):
    api.post_project("Проект для задачи")
    boards_api.post_new_board(api.project_id, "Доска")
    columns_api.post_new_columns("To do", boards_api.board_id)
    tasks_api.post_task("Задача по диплому", columns_api.column_id)

    response = tasks_api.complete_task(tasks_api.task_id)

    assert response.status_code == 200
    assert tasks_api.task_id is not None

    api.delete_project()


@allure.title("Отправить задачу в архив")
@pytest.mark.api
@pytest.mark.positive
def test_delete_task(api, boards_api, columns_api, tasks_api):
    api.post_project("Проект для задачи")
    boards_api.post_new_board(api.project_id, "Доска")
    columns_api.post_new_columns("To do", boards_api.board_id)
    tasks_api.post_task("Задача по диплому", columns_api.column_id)
    response = tasks_api.archive_task(tasks_api.task_id)
    assert response.status_code == 200
    check = tasks_api.get_task_by_id(tasks_api.task_id)
    assert check.json()["archived"] is True
    api.delete_project()
