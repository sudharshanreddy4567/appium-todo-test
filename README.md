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
---

## ⚙️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/your-username/appium-todo-test.git
cd appium-todo-test
2. Create Virtual Environment
bash

python -m venv venv
venv\Scripts\activate           # For Windows
# source venv/bin/activate     # For macOS/Linux
3. Install Dependencies

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
🧪 Run the Tests
1. Start the Appium Server

appium
2. Run Tests Using Pytest

pytest -v
📊 Allure Reporting (Optional)
1. Install Allure CLI
On Windows:

scoop install allure
On macOS:


brew install allure
2. Run Tests and Serve Allure Report

pytest --alluredir=allure-results
allure serve allure-results
✅ Features Tested
📌 Add a new task

✅ Mark a task as completed

🗑️ Delete a task

🤝 Contributing
Pull requests are welcome! For significant changes, open an issue to discuss your ideas first.

📄 License
This project is open-source and available under the MIT License.

🙌 Credits
Developed as part of a medium-level Appium automation project using an open-source ToDo application.



---

Let me know if you also want me to generate:

- `requirements.txt`
- `appium_driver.py` sample
- All test and page object boilerplate code

I can deliver all the code with human-written formatting if needed for GitHub.
