# 📱 Appium ToDo App Test Automation (Python + Pytest)

This is a mobile test automation project for a ToDo Android application using **Appium**, **Python**, and **Pytest**.  
It follows the **Page Object Model (POM)** structure to keep test code clean, scalable, and easy to maintain.  
The tests cover three main functionalities: **adding**, **completing**, and **deleting** tasks.  
Supports both Android emulators and real devices with optional **Allure reports** for test reporting.

---

## 🚀 Tech Stack

- **Programming Language**: Python
- **Automation Tool**: Appium
- **Test Framework**: Pytest
- **Device**: Android Emulator or Real Device
- **Build Tool**: virtualenv + pip
- **Reporting Tool**: Allure (optional)

---

## 📁 Project Structure

├── test_cases/ # Test scripts for app features
│ ├── test_add_task.py
│ ├── test_delete_task.py
│ └── test_complete_task.py
│
├── pages/ # Page Object classes
│ ├── base_page.py
│ ├── home_page.py
│ └── add_task_page.py
│
├── drivers/ # Appium driver setup
│ └── appium_driver.py
│
├── utils/ # Config and utilities
│ └── config.py
│
├── apk/ # ToDo app APK
│ └── todo-app.apk
│
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore


---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/appium-todo-test.git
cd appium-todo-test
2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate           # For Windows
# source venv/bin/activate     # For macOS/Linux
3. Install Dependencies
pip install -r requirements.txt
pip install -r requirements.txt
4. Place APK File
Download or build the APK of the ToDo app (e.g., todo-app.apk) and place it in the apk/ folder.

🔧 Update the following fields in drivers/appium_driver.py based on the APK:

appPackage: e.g., com.example.todo

appActivity: e.g., .MainActivity

You can use this command to find package and activity:
adb shell dumpsys window windows | find "mCurrentFocus"
📱 Install the APK on Emulator or Device
Make sure your Android emulator or physical device is running and detected:
adb devices
adb install apk/todo-app.apk
📊 Allure Reporting (Optional)
1. Install Allure CLI
On Windows
scoop install allure
2. Run Tests and Serve Allure Report
pytest --alluredir=allure-results
allure serve allure-results
