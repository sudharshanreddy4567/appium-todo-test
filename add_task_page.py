from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AddTaskPage(BasePage):
    TASK_INPUT = (By.ID, "com.todo.app:id/taskInput")
    SAVE_BUTTON = (By.ID, "com.todo.app:id/saveButton")

    def add_task(self, task_text):
        self.send_keys(self.TASK_INPUT, task_text)
        self.click(self.SAVE_BUTTON)
