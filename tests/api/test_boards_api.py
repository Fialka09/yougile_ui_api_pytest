import allure
import pytest


@allure.feature("API")
@allure.story("Доски")
@allure.title("Создание доски")
def test_create_board(api, boards_api):
    api.post_project("Проект для доски")
    response = boards_api.post_new_board(api.project_id, "Моя доска")

    assert response.status_code == 201
    assert boards_api.board_id is not None

    boards_api.delete_board_by_id(boards_api.board_id)
    api.delete_project()


@allure.title("Обновление доски")
def test_update_board(api, boards_api):
    api.post_project("Сменить название доски")
    boards_api.post_new_board(api.project_id, "Моя доска")
    response = boards_api.update_board_by_id(
        boards_api.board_id, "Обновленная доска"
    )
    assert response.status_code == 200
    assert boards_api.board_id is not None
    boards_api.delete_board_by_id(boards_api.board_id)
    api.delete_project()


@allure.title("Удаление доски")
def test_delete_board(api, boards_api):
    api.post_project("Отметить доску удаленной")
    boards_api.post_new_board(api.project_id, "Доска 1")
    boards_api.post_new_board(api.project_id, "Доска 2")

    response = boards_api.delete_board_by_id(boards_api.board_id)
    assert response.status_code == 200

    api.delete_project()


@allure.title("Создание доски с разными названиями")
@pytest.mark.api
@pytest.mark.parametrize(
    "board_title",
    [
        "Доска2026",
        "Новая доска",
        "New Board",
        "12345",
        "Доска-тест_1",
    ],
)
def test_create_board_with_different_titles(api, boards_api, board_title):
    api.post_project("Проект для доски")
    response = boards_api.post_new_board(api.project_id, board_title)
    assert response.status_code == 201
    assert boards_api.board_id is not None
    api.delete_project()
