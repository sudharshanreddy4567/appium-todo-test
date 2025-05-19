class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_button(self):
        self.driver.find_element_by_id("com.todo.app:id/addTaskButton").click()

    def enter_task(self, task_text):
        self.driver.find_element_by_id("com.todo.app:id/taskInput").send_keys(task_text)

    def save_task(self):
        self.driver.find_element_by_id("com.todo.app:id/saveButton").click()

    def task_present(self, task_text):
        tasks = self.driver.find_elements_by_id("com.todo.app:id/taskText")
        return any(task.text == task_text for task in tasks)
