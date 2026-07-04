# 🚀 Playwright Python Automation Framework | Page Object Model (POM) | Pytest | Data-Driven Testing

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Playwright](https://img.shields.io/badge/Playwright-Web%20Automation-45ba4b?style=for-the-badge&logo=playwright)
![Pytest](https://img.shields.io/badge/Pytest-Test%20Framework-green?style=for-the-badge&logo=pytest)
![POM](https://img.shields.io/badge/Page-Object%20Model-orange?style=for-the-badge)
![Data Driven](https://img.shields.io/badge/Data-Driven-purple?style=for-the-badge)
![Automation](https://img.shields.io/badge/UI-Automation-red?style=for-the-badge)

</p>

---

# 🚀 Enterprise Playwright Automation Framework

Modern web applications require automation frameworks that are fast, maintainable, scalable, and easy to extend.

This repository demonstrates a **production-style UI Automation Framework** built using **Playwright**, **Python**, **Pytest**, and the **Page Object Model (POM)** design pattern.

Rather than creating isolated automation scripts, this project focuses on building a reusable framework capable of supporting enterprise-level automation projects.

Whether you're a QA Engineer, SDET, Automation Engineer, or Hiring Manager evaluating technical skills, this repository showcases practical automation engineering and clean framework design.

---

# 🎯 Project Highlights

✔ Playwright Automation Framework

✔ Python-based Test Automation

✔ Page Object Model (POM)

✔ Pytest Framework

✔ Data-Driven Testing

✔ HTML Test Reporting

✔ Utility Classes

✔ Configurable Test Execution

✔ Modular Architecture

✔ End-to-End Test Scenarios

---

# 🏗 Framework Architecture

```
python_playwright_pom_framework
│
├── PageObjectModel
│   ├── Homepage.py
│   ├── LoginPage.py
│   ├── CartPage.py
│   └── TestPage.py
│
├── PlaywrightPythonFramework
│
│   ├── TestCases
│   │
│   │   ├── test_login.py
│   │   ├── test_login_data_driven.py
│   │   ├── test_product_search.py
│   │   ├── test_add_product_to_cart.py
│   │   ├── test_user_registration.py
│   │   ├── test_user_logout.py
│   │   ├── test_end_to_end.py
│   │
│   └── reports
│       └── myreport.html
│
├── pages
│   ├── Homepage.py
│   ├── loginpage.py
│   ├── registration_page.py
│   ├── product_page.py
│   ├── shopping_cart_page.py
│   ├── checkout_page.py
│   ├── logout_page.py
│   ├── search_results_page.py
│   └── my_account_page.py
│
├── TestData
│   ├── logindata.csv
│   ├── logindata.json
│   └── logindata.xlsx
│
├── Utils
│   ├── data_reader_util.py
│   └── random_data_util.py
│
├── config.py
├── conftest.py
├── pytest.ini
│
└── README.md
```

---

# ✨ Framework Features

## 🎭 UI Automation

The framework automates complete user journeys using Playwright.

Implemented scenarios include:

- User Login
- User Logout
- Product Search
- Add Product to Cart
- User Registration
- Shopping Cart Validation
- End-to-End Purchase Flow

---

## 📄 Page Object Model (POM)

The framework follows the Page Object Model design pattern.

Benefits include:

- Better Maintainability
- High Reusability
- Cleaner Test Scripts
- Easier Framework Expansion
- Separation of Test Logic & UI Locators

---

## 📊 Data-Driven Testing

The framework supports multiple external data sources.

Supported formats:

- CSV
- JSON
- Excel

This enables:

- Reusable test cases
- Multiple datasets
- Better test coverage
- Easier maintenance

---

## 🧰 Utility Layer

Reusable utilities simplify framework maintenance.

Includes:

- Random Data Generator
- Data Reader Utilities
- Shared Helper Functions

---

## 📈 HTML Reporting

After execution, automated HTML reports are generated.

Benefits:

- Easy execution review
- Test result visualization
- Faster debugging
- Better stakeholder reporting

---

## ⚙ Configuration Management

Centralized configuration allows:

- Environment management
- Browser configuration
- URL management
- Framework customization

---

# 🧪 Test Coverage

### Authentication

- Login
- Logout

### Product Validation

- Product Search
- Product Details

### Shopping

- Add To Cart
- Cart Validation

### User Management

- Registration
- Account Validation

### End-to-End

- Complete User Journey

### Data-Driven Testing

- CSV
- JSON
- Excel

---

# 💻 Technology Stack

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Playwright | UI Automation |
| Pytest | Test Execution |
| Page Object Model | Framework Design |
| HTML Reports | Reporting |
| JSON | Test Data |
| CSV | Data-Driven Testing |
| Excel | Data-Driven Testing |
| Git | Version Control |
| GitHub | Repository Hosting |

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/ArpitChoubey/python_playwright_pom_framework.git
```

---

## Navigate

```bash
cd python_playwright_pom_framework
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Playwright Browsers

```bash
playwright install
```

---

## Execute All Tests

```bash
pytest
```

---

## Generate HTML Report

```bash
pytest --html=reports/myreport.html
```

---

# 📂 Framework Components

## Pages

Contains reusable Page Object classes.

Examples:

- Login Page
- Home Page
- Product Page
- Checkout Page
- Shopping Cart
- Registration Page

---

## Test Cases

Automated business scenarios including:

- Login Validation
- Product Search
- Add To Cart
- Registration
- Logout
- End-to-End Purchase Flow

---

## Test Data

Supports:

- Excel
- CSV
- JSON

Ideal for scalable Data-Driven Testing.

---

## Utilities

Reusable helper classes for:

- Random Test Data
- Reading External Files
- Framework Utilities

---

# 📈 Skills Demonstrated

This project demonstrates hands-on experience with:

### Test Automation

- UI Automation
- Web Testing
- End-to-End Testing

### Framework Development

- Playwright
- Python
- Pytest
- Page Object Model

### Test Design

- Reusable Components
- Modular Framework
- Maintainable Architecture

### Quality Engineering

- Data-Driven Testing
- Reporting
- Test Organization
- Automation Best Practices

---

# 🌟 Why This Repository Matters

Many Playwright repositories only automate a login page.

This repository demonstrates how to build a maintainable automation framework capable of supporting enterprise-level UI testing.

It showcases:

- Scalable Framework Design
- Clean Code Practices
- Reusable Components
- Modern Automation Architecture
- Real-World Test Scenarios

---

# 🚀 Future Enhancements

Planned improvements include:

- GitHub Actions CI/CD
- Jenkins Integration
- Docker Support
- Parallel Execution
- Cross-Browser Execution
- Screenshot Capture on Failure
- Video Recording
- Retry Mechanism
- Allure Reports
- Environment Profiles

---

# 💼 Recruiter Snapshot

In less than one minute, this repository demonstrates experience with:

✅ Playwright

✅ Python

✅ Pytest

✅ Page Object Model

✅ Data-Driven Testing

✅ HTML Reporting

✅ UI Automation

✅ Framework Development

✅ Modular Test Design

✅ End-to-End Testing

✅ Automation Best Practices

---

# 🎯 Ideal Audience

This project is valuable for:

- QA Automation Engineers
- SDETs
- Playwright Developers
- Manual Testers transitioning to Automation
- Students learning Playwright
- Hiring Managers evaluating automation skills

---

# 👨‍💻 About Me

## Arpit Choubey

**Senior QA Automation Engineer | SDET | Playwright | Python | Selenium | Java | API Testing | Quality Engineering**

I enjoy designing scalable automation frameworks, improving software quality, and contributing practical automation projects to the open-source community.

---

# 🌐 Connect With Me

### GitHub

https://github.com/ArpitChoubey

### LinkedIn

https://www.linkedin.com/in/arpitchoubey/

### Medium

https://medium.com/@ArpitChoubey9

---

# ⭐ Support

If you found this project useful:

⭐ Star this repository

🍴 Fork it

💬 Share feedback

🤝 Connect with me

Every ⭐ motivates me to continue building practical automation frameworks for the QA community.

---

# 📌 Repository

**GitHub Repository**

https://github.com/ArpitChoubey/python_playwright_pom_framework

---

# 💡 Key Takeaway

> **"Great automation isn't measured by the number of test scripts—it's measured by the quality, scalability, and maintainability of the framework behind them."**
