#  Selenium Unit Testing Project

## 📌 Overview
This project demonstrates how to perform **automated unit testing with Selenium WebDriver in Python** using both `pytest` and `unittest`.  
It follows the **Page Object Model (POM)** design pattern to keep the test cases clean, modular, and easy to maintain.  

The tests in this project focus on validating the **login functionality** of the sample website:  
🔗 [SauceDemo - Login Page](https://www.saucedemo.com/)

---

##  Features
- ✅ **Page Object Model (POM)** for better code structure  
- ✅ **Unit testing with `pytest`** and `unittest` compatibility  
- ✅ **HTML Reports** generated using `pytest-html`  
- ✅ **Screenshots captured on test failure**  
- ✅ **Reusable WebDriver setup** using `webdriver-manager`  
- ✅ Easily extensible for more test cases  

---

##  Project Structure
```
selenium-unit-testing/
│── tests/
│   └── test_login.py         # Test cases for login functionality
│
│── utils/
│   ├── __init__.py
│   └── driver_setup.py       # WebDriver setup and teardown
│
│── pages/
│   ├── __init__.py
│   └── login_page.py         # Page Object for Login Page
│
│── conftest.py               # Pytest fixtures
│── requirements.txt          # Project dependencies
│── README.md                 # Project documentation
```

---

##  Setup & Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/selenium-unit-testing.git
   cd selenium-unit-testing
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Mac/Linux
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶ Running the Tests

Run the tests with **Pytest**:
```bash
pytest --html=report.html --self-contained-html -v tests/
```

This will:
- Launch the browser  
- Navigate to the login page  
- Enter credentials  
- Validate login success/failure  
- Generate a `report.html` file  

---

## Test Reports
After running the tests, an HTML report will be generated:  
```
report.html
```
Simply open this file in any browser to view detailed test execution results with pass/fail status.

---

## Screenshots on Failure
If a test fails, a screenshot of the browser is automatically saved inside the `screenshots/` folder for debugging.

---

## 🔮 Future Enhancements
- Add more test cases (e.g., logout, invalid credentials, password reset).  
- Cross-browser testing with Firefox and Edge.  
- Integration with CI/CD pipelines (GitHub Actions).  
- Docker support for headless execution.  
