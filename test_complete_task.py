import pytest
from drivers.appium_driver import create_driver
from pages.home_page import HomePage

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

def test_complete_task(driver):
    home = HomePage(driver)
    home.click_add_button()
    home.enter_task("Complete this task")
    home.save_task()

    assert home.task_present("Complete this task")

    home.click_task_by_name("Complete this task")
    # Optionally: Check if task UI changes (strikethrough or icon)
