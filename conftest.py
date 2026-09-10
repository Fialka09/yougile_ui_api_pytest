import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import get_token, BASE_URL, LOGIN, PASSWORD
from api.projects_api import ProjectsAPI
from api.boards_api import BoardsAPI
from api.columns_api import ColumnsAPI
from api.tasks_api import TasksAPI
from ui.pages.login_page import LoginPage
from api.chats_api import ChatsAPI


@pytest.fixture
def token():
    return get_token()


@pytest.fixture
def api(token):
    return ProjectsAPI(BASE_URL, token)


@pytest.fixture
def boards_api(token):
    return BoardsAPI(BASE_URL, token)


@pytest.fixture
def columns_api(token):
    return ColumnsAPI(BASE_URL, token)


@pytest.fixture
def tasks_api(token):
    return TasksAPI(BASE_URL, token)


@pytest.fixture
def chrome_driver():
    options = Options()
    options.add_argument("--headless")

    with allure.step("Открыть и настроить браузер"):
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(4)
        driver.maximize_window()

    yield driver

    with allure.step("Закрыть браузер"):
        driver.quit()


@pytest.fixture
def logged_in_driver(chrome_driver):
    login_page = LoginPage(chrome_driver)
    login_page.open()
    login_page.click_login_on_main()
    login_page.enter_email(LOGIN)
    login_page.enter_password(PASSWORD)
    login_page.click_login()
    yield chrome_driver


@pytest.fixture
def chats_api(token):
    return ChatsAPI(BASE_URL, token)
