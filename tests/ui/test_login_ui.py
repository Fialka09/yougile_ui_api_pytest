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
    page.enter_email(LOGIN)
    page.enter_password(PASSWORD)
    page.click_login()

    assert "yougile.com" in chrome_driver.current_url

@allure.title("Авторизация с неверным паролем")
def test_login_wrong_password(logged_in_driver):
    login_page = LoginPage(logged_in_driver)
    login_page.open()
    login_page.click_login_on_main()
    login_page.enter_email(LOGIN)
    login_page.enter_password("wrong_password")
    login_page.click_login()

    assert "Неверный e-mail или пароль" in login_page.get_error_text()

@allure.title("Авторизация с пустым email")
def test_login_empty_email(logged_in_driver):
    login_page = LoginPage(logged_in_driver)
    login_page.open()
    login_page.click_login_on_main()
    login_page.enter_email("")
    login_page.enter_password(PASSWORD)
    login_page.click_login()
    assert "Неверный e-mail или пароль" in login_page.get_error_text()

@allure.title("Авторизация с пустым паролем")
def test_login_empty_password(logged_in_driver):
    login_page = LoginPage(logged_in_driver)
    login_page.open()
    login_page.click_login_on_main()
    login_page.enter_email(LOGIN)
    login_page.enter_password("")
    login_page.click_login()
    assert "Incorrect request" in login_page.get_error_text()

