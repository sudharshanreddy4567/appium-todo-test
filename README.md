# appium-todo-test
# 📱 Appium Automation for To-Do App

This repository contains UI test automation for an Android To-Do application using Appium. The goal is to test core functionalities like adding, deleting, and completing tasks.

## 🔧 Setup Instructions

1. Clone the repo
2. Install dependencies
3. Set up Appium and Android emulator
4. Run tests

## 📁 Folder Structure

- `test_cases/`: Contains test scripts
- `pages/`: Page Object Model for app screens
- `drivers/`: Appium driver setup
- `utils/`: Helper functions and config

## 🧪 Sample Test Case

```python
def test_add_task(driver):
    home_page = HomePage(driver)
    home_page.click_add_button()
    ...
