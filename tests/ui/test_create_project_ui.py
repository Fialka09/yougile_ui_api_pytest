import allure
import pytest
import time
from ui.pages.project_form import ProjectForm


@allure.feature("UI")
@allure.story("Проекты")
@allure.title("Создание проекта")
@pytest.mark.ui
@pytest.mark.positive
def test_create_project(logged_in_driver, chats_api):
    project_form = ProjectForm(logged_in_driver)
    project_name = f"Проект {int(time.time())}"

    project_form.click_add()
    project_form.select_project_type()
    project_form.enter_project_name(project_name)
    project_form.select_create_button()

    with allure.step("Проверить, что проект отображается"):
        assert project_form.is_project_displayed(project_name)

    with allure.step("Удалить созданный проект"):
        project_form.delete_project(project_name)

    with allure.step("Удалить чат проекта"):
        chats_api.delete_chat_by_title(project_name)


@allure.title("Закрытие формы крестиком")
@pytest.mark.ui
@pytest.mark.positive
def test_close_project(logged_in_driver):
    project_form = ProjectForm(logged_in_driver)
    project_form.click_add()
    project_form.select_project_type()
    project_form.click_close()


@allure.title("Закрытие формы кнопкой Отмена")
@pytest.mark.ui
@pytest.mark.positive
def test_close_project_form(logged_in_driver):
    project_form = ProjectForm(logged_in_driver)
    project_form.click_add()
    project_form.select_project_type()
    project_form.click_cancel()


@allure.title("Снятие галочки чата")
@pytest.mark.ui
@pytest.mark.positive
def test_uncheck_chat(logged_in_driver):
    form = ProjectForm(logged_in_driver)
    form.click_add()
    form.select_project_type()
    form.uncheck_chat()


@allure.title("Проверка неактивности кнопки")
@pytest.mark.ui
@pytest.mark.positive
def test_create_button_disabled(logged_in_driver):
    form = ProjectForm(logged_in_driver)
    form.click_add()
    form.select_project_type()

    assert not form.is_create_button_enabled()
