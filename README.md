# api-automation-framework
Professional REST API automation framework using Python, Pytest and Requests library with Page Object Model pattern.
# 🔌 API Automation Framework 
Professional REST API testing framework built with Python, Pytest and Requests library. 
## 🛠️ Tech Stack 
- Python 3.11
- Pytest
- Requests Library
- Page Object Model Pattern
## 📁 Project Structure 
Selenium-API/ 
    config.py ← Central configuration 
    api/ 
      api\_client.py ← Reusable API helper 
    tests/ 
      test\_users.py ← Test cases 
## ✅ What It Tests 
- GET all users
- GET single user
- POST create new user
- PUT update user
- DELETE user
- GET missing user (404)
## ▶️ How To Run 
pip install pytest requests 
pytest tests/test\_users.py -v -s 
## 📊 Test Results 
- test\_get\_all\_users ✅ PASSED
- test\_get\_single\_user ✅ PASSED
- test\_create\_user ✅ PASSED
- test\_update\_user ✅ PASSED
- test\_delete\_user ✅ PASSED
- test\_get\_missing\_user ✅ PASSED
