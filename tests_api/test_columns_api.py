import allure


@allure.feature("API")
@allure.story("Колонки")
@allure.title("Создание колонки")
def test_create_column(api, boards_api, columns_api):
    api.post_project("Проект для колонки")
    boards_api.post_new_board(api.project_id, "Доска")

    response = columns_api.post_new_columns(
        "Дела текущие", boards_api.board_id
    )

    assert response.status_code == 201
    assert columns_api.column_id is not None

    api.delete_project()


@allure.title("Обновление колонки")
def test_update_column(api, boards_api, columns_api):
    api.post_project("Проект для колонки")
    boards_api.post_new_board(api.project_id, "Доска")
    columns_api.post_new_columns("Дела в работе", boards_api.board_id)
    response = columns_api.update_column_id(
        columns_api.column_id, "Дела завершённые"
    )

    assert response.status_code == 200
    assert columns_api.column_id is not None

    api.delete_project()


@allure.title("Удаление колонки")
def test_delete_column(api, boards_api, columns_api):
    api.post_project("Проект для колонки")
    boards_api.post_new_board(api.project_id, "Доска")
    columns_api.post_new_columns("Дела в работе", boards_api.board_id)
    response = columns_api.delete_column_id(columns_api.column_id)
    assert response.status_code == 200
    api.delete_project()
