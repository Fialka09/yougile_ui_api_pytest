import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BoardPage:

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.add_task_button = (
            By.XPATH,
            "//span[contains(text(), 'Добавить задачу')]",
        )
        self.task_input = (
            By.XPATH,
            "//textarea[@data-testid='board-task-input-name']",
        )

    @allure.step("Нажать Добавить задачу")
    def click_add_task(self) -> None:
        self.wait.until(
            EC.element_to_be_clickable(self.add_task_button)
        ).click()

    @allure.step("Ввести название задачи")
    def enter_task_name(self, name: str) -> None:
        field = self.wait.until(EC.element_to_be_clickable(self.task_input))
        field.send_keys(name)
        field.send_keys(Keys.RETURN)
        self.driver.find_element(By.TAG_NAME, "body").click()

    @allure.step("Проверить, что задача отображается на доске")
    def is_task_displayed(self, task_name: str) -> bool:
        """Проверить, что задача отображается на доске."""
        return self.wait.until(lambda driver: task_name in driver.page_source)
