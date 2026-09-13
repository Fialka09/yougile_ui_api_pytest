import allure
import pytest
from config import BASE_URL
from api.yougile_api import YougileAPI


@allure.feature("API")
@allure.story("Пользователи")
@allure.title("Получение текущего пользователя")
@pytest.mark.api
@pytest.mark.positive
def test_get_current_user(token):
    api = YougileAPI(BASE_URL, token)
    response = api.get_users()
    assert response.status_code == 200
    assert api.user_id is not None
