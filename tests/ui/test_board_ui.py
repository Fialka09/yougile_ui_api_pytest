import time
import pytest
import allure
from ui.pages.project_form import ProjectForm
from ui.pages.board_page import BoardPage


@allure.feature("UI")
@allure.story("Доска")
@allure.title("Добавление задачи")
@pytest.mark.ui
def test_add_task(logged_in_driver, chats_api):
    form = ProjectForm(logged_in_driver)
    project_name = f"Проект {int(time.time())}"

    form.click_add()
    form.select_project_type()
    form.enter_project_name(project_name)
    form.select_create_button()

    board = BoardPage(logged_in_driver)
    board.click_add_task()
    board.enter_task_name("Задача по диплому")

    with allure.step("Проверить, что задача отображается"):
        assert board.is_task_displayed("Задача по диплому")

    with allure.step("Удалить проект"):
        form.delete_project(project_name)

    with allure.step("Удалить чат проекта"):
        chats_api.delete_chat_by_title(project_name)
