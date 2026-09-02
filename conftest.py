import pytest
from config import get_token, BASE_URL
from api.projects_api import ProjectsAPI
from api.boards_api import BoardsAPI
from api.columns_api import ColumnsAPI
from api.tasks_api import TasksAPI


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