import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class ProjectForm:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.add_button = (
            By.XPATH,
            "//div[@data-testid='add-project-button']",
        )
        self.project_type = (By.XPATH, "//div[text()='Проект с задачами']")
        self.name_field = (
            By.XPATH,
            "//input[@placeholder='Введите название проекта…']",
        )
        self.create_button = (
            By.XPATH,
            "//div[text()='Добавить проект с задачами']",
        )
        self.cancel_button = (By.XPATH, "//div[text()='Отмена']")
        self.close_button = (
            By.XPATH,
            "//div[contains(@class, 'group/icon-button')]"
        )
        self.chat_checkbox = (By.XPATH, "//div[@role='checkbox']")
        self.id_prefix = (
            By.XPATH,
            "//input[@type='text' and @value!=''][2]"
        )
        self.my_company = (
            By.XPATH,
            "//div[text()='Моя компания']"
        )
        self.project_card = (
            By.XPATH,
            "//div[@data-testid='project-card']"
        )
        self.project_title = (
            By.XPATH,
            ".//div[@data-testid='project-title']"
        )
        self.delete_button = (
            By.XPATH,
            "//div[text()='Удалить']"
        )
        self.confirm_delete_button = (
            By.XPATH,
            "//div[contains(@class, 'text-left') and text()='Удалить']"
        )

    @allure.step("Нажать на +")
    def click_add(self):
        self.wait.until(EC.element_to_be_clickable(self.add_button)).click()

    @allure.step("Выбрать 'Проект с задачами'")
    def select_project_type(self):
        self.wait.until(EC.element_to_be_clickable(self.project_type)).click()

    @allure.step("Ввести название проекта")
    def enter_project_name(self, name):
        field = self.wait.until(EC.element_to_be_clickable(self.name_field))
        field.clear()
        field.send_keys(name)

    @allure.step("Нажать на кнопку 'Добавить проект с задачами'")
    def select_create_button(self):
        self.wait.until(EC.element_to_be_clickable(self.create_button)).click()

    @allure.step("Закрыть форму")
    def click_close(self):
        close = self.wait.until(
            EC.presence_of_element_located(self.close_button)
        )
        self.driver.execute_script("arguments[0].click();", close)

    @allure.step("Нажать Отмена")
    def click_cancel(self):
        self.wait.until(EC.element_to_be_clickable(self.cancel_button)).click()

    @allure.step("Снять галочку чата")
    def uncheck_chat(self):
        self.wait.until(EC.element_to_be_clickable(self.chat_checkbox)).click()

    @allure.step("Проверить активность кнопки")
    def is_create_button_enabled(self):
        button = self.wait.until(
            EC.presence_of_element_located(self.create_button)
        )
        parent = button.find_element(By.XPATH, "..")
        return "pointer-events-none" not in parent.get_attribute("class")

    @allure.step("Удалить проект через меню")
    def delete_project(self, project_name: str):
        # Перейти в «Моя компания»
        company = self.wait.until(
            EC.element_to_be_clickable(self.my_company)
        )
        company.click()

        # Дождаться карточек
        self.wait.until(
            EC.presence_of_element_located(self.project_card)
        )

        # Найти карточку
        cards = self.driver.find_elements(
            By.XPATH, "//div[@data-testid='project-card']"
        )
        target_card = None
        for card in cards:
            title = card.find_element(
                By.XPATH, ".//div[@data-testid='project-title']"
            ).get_attribute("textContent")
            if project_name in title:
                target_card = card
                break

        if not target_card:
            raise Exception(f"Проект '{project_name}' не найден!")

        # Навести курсор
        actions = ActionChains(self.driver)
        actions.move_to_element(target_card).perform()

        # Кликнуть троеточие
        menu = target_card.find_element(
            By.XPATH, ".//div[@data-testid='project-card-menu-button']"
        )
        self.driver.execute_script("arguments[0].click();", menu)

        time.sleep(1)

        # Нажать «Удалить»
        delete = self.wait.until(
            EC.element_to_be_clickable(self.delete_button)
        )
        self.driver.execute_script("arguments[0].click();", delete)

        time.sleep(1)

        # Подтвердить удаление
        confirm = self.wait.until(
            EC.element_to_be_clickable(self.confirm_delete_button)
        )
        self.driver.execute_script("arguments[0].click();", confirm)

        time.sleep(2)