import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Страница входа в Yougile."""

    URL = "https://ru.yougile.com/"

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.login_on_main = (By.LINK_TEXT, "Войти")
        self.email = (By.XPATH, "//input[@type='email']")
        self.password = (By.XPATH, "//input[@type='password']")
        self.login_button = (
            By.XPATH,
            "//div[@role='button']//div[text()='Войти']",
        )
        self.error_message = (
            By.XPATH,
            "//div[contains(@class, 'login-error')]"
        )

    @allure.step("Нажать Войти на главной")
    def click_login_on_main(self) -> None:
        link = self.wait.until(EC.element_to_be_clickable(self.login_on_main))
        link.click()

    @allure.step("Открыть страницу входа")
    def open(self) -> None:
        self.driver.get(self.URL)

    @allure.step("Ввести email")
    def enter_email(self, email: str) -> None:
        field = self.wait.until(EC.element_to_be_clickable(self.email))
        field.clear()
        field.send_keys(email)

    @allure.step("Ввести пароль")
    def enter_password(self, password: str) -> None:
        field = self.wait.until(EC.element_to_be_clickable(self.password))
        field.clear()
        field.send_keys(password)

    @allure.step("Нажать кнопку Войти")
    def click_login(self) -> None:
        button = self.wait.until(EC.element_to_be_clickable(self.login_button))
        button.click()

    @allure.step("Получить текст ошибки")
    def get_error_text(self) -> str:
        wait = WebDriverWait(self.driver, 20)  # отдельное ожидание
        error = wait.until(
            EC.presence_of_element_located(self.error_message)
        )
        return error.text

