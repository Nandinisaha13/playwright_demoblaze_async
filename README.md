# 🚀 Playwright Async Automation Framework (DemoBlaze)

This project is a **production-style UI automation framework** built using **Playwright (Python - Async)**.
It demonstrates real-world QA automation practices including async execution, Page Object Model (POM), and end-to-end test flows.

---

## 🔗 Portfolio

👉 Check out my full QA portfolio here: **[YOUR_PORTFOLIO_LINK_HERE]**

---

## 🧠 Tech Stack

* Python 3.11+
* Playwright (Async API)
* Pytest
* Pytest-Asyncio
* Pytest-HTML (Reporting)

---

## 🏗️ Framework Features

* ✅ Async Playwright implementation
* ✅ Page Object Model (POM) design
* ✅ Data-driven testing using `pytest.mark.parametrize`
* ✅ Alert handling (JS dialogs)
* ✅ Modular & scalable structure
* ✅ HTML reporting
* ✅ Clean project architecture

---

## 📁 Project Structure

```
Playwright_demoblaze_async/
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── signup_page.py
│   ├── home_page.py
│   ├── product_page.py
│   ├── cart_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_negative_login.py
│   ├── test_signup.py
│   ├── test_cart.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
```

---

## 🧪 Test Scenarios Covered

### 🔐 Authentication

* Valid login
* Invalid login scenarios (data-driven)
* Signup flow with dynamic user creation

### 🛒 Cart Flow

* Add product to cart
* Validate product in cart

---

## ⚠️ Observations / Real-World Challenges

* DemoBlaze has inconsistent alert behavior for empty fields
* Async event handling required different strategies:

  * `expect_event` for backend alerts
  * `page.once("dialog")` for frontend validation

---

## ▶️ How to Run Tests

### Install dependencies

```
pip install -r requirements.txt
playwright install
```

### Run all tests

```
pytest -s
```

### Run specific test

```
pytest tests/test_cart.py -s
```

---

## 📊 Reports

HTML report is generated after execution:

```
report.html
```

---

## 💡 Key Learnings

* Handling async events in UI automation
* Managing flaky UI behavior
* Designing scalable test frameworks
* Writing resilient and maintainable tests

---

## 👩‍💻 About Me

I am a **Senior QA Engineer with 5+ years of experience**, specializing in:

* Manual Testing
* Automation Testing
* API Testing
* Building scalable QA frameworks

---

## ⭐ Future Enhancements

* Parallel execution using pytest-xdist
* CI/CD integration
* API + UI integration tests
* Retry mechanism for flaky tests

---

⭐ If you found this useful, feel free to star the repo!
