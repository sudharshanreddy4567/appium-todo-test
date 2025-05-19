import pytest
from drivers.appium_driver import create_driver
from pages.home_page import HomePage

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

def test_delete_task(driver):
    home = HomePage(driver)
    home.click_add_button()
    home.enter_task("Task to delete")
    home.save_task()

    assert home.task_present("Task to delete")
    
    home.click_task_by_name("Task to delete")  # If this deletes task
    assert "Task to delete" not in home.get_all_tasks()
