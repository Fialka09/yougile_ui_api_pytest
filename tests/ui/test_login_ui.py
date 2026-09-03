import allure
from config import LOGIN, PASSWORD
from ui.pages.login_page import LoginPage


@allure.feature("UI")
@allure.story("Авторизация")
@allure.title("Вход с валидными данными")
def test_login(chrome_driver):
    page = LoginPage(chrome_driver)
    page.open()
    page.click_login_on_main()
    print(chrome_driver.current_url)
    page.enter_email(LOGIN)
    page.enter_password(PASSWORD)
    page.click_login()

    assert "yougile.com" in chrome_driver.current_url
