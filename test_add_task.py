import pytest
from drivers.appium_driver import create_driver
from pages.home_page import HomePage

@pytest.fixture(scope="function")
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

def test_add_task(driver):
    home = HomePage(driver)
    home.click_add_button()
    home.enter_task("Buy groceries")
    home.save_task()
    assert home.task_present("Buy groceries")
