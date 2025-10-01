# Module 4 – Command-Line Calculator (Professional-Grade)

![CI](https://github.com/jasonj2010/module4_is601/actions/workflows/tests.yml/badge.svg)
[![codecov](https://codecov.io/gh/jasonj2010/module4_is601/branch/main/graph/badge.svg)](https://codecov.io/gh/jasonj2010/module4_is601)

---

## 📖 Project Overview
This project is a **modular, professional-grade command-line calculator** built in Python.  
It demonstrates:
- A REPL (Read-Eval-Print Loop) interface for continuous user interaction  
- Core arithmetic operations (addition, subtraction, multiplication, division)  
- CalculationFactory for dynamic creation of operations  
- CalculationHistory to track all calculations in-session  
- Special commands: help, history, and exit  
- Input validation and robust error handling using both LBYL (Look Before You Leap) and EAFP (Easier to Ask Forgiveness than Permission)  
- Comprehensive unit & parameterized testing with pytest  
- Continuous Integration via GitHub Actions, enforcing 100% test coverage  

---

## ⚙️ Setup Instructions

1. Clone the Repository  

       git clone git@github.com:jasonj2010/module4_is601.git
       cd module4_is601  

2. Create & Activate a Virtual Environment  

   - Windows (PowerShell):  

         python -m venv venv
         .\venv\Scripts\Activate.ps1  

   - Mac/Linux:  

         python3 -m venv venv
         source venv/bin/activate  

3. Install Dependencies  

       pip install -r requirements.txt  

---

## ▶️ Run the Program

       python main.py  

Example REPL session:  

       Welcome to the calculator REPL! Type 'help' for commands or 'exit' to quit  
       Enter command: add  
       Enter first number: 2  
       Enter second number: 3  
       Result: 5.0  

Available commands:  
- add, subtract, multiply, divide  
- history → view past calculations  
- help → show available commands  
- exit → quit the REPL  

---

## 🧪 Run Tests (100% Coverage Enforced)

       pytest  

or with detailed coverage:  

       pytest --cov=app --cov-report=term-missing  

---

## 📂 Project Structure

    app/  
     ├── calculator/        # REPL interface  
     ├── calculation/       # Calculation & Factory classes  
     ├── operation/         # Arithmetic operation methods  
     └── __init__.py  
    tests/                  # Unit & parameterized tests (incl. CLI tests)  
    main.py                 # Entry point  
    pytest.ini              # Pytest config (100% coverage enforcement)  
    requirements.txt  
    .github/workflows/      # GitHub Actions CI workflow  

---

## ✅ Key Features & Notes
- Object-Oriented Design: Factory & History patterns for clean, extensible architecture  
- Error Handling: Clear messages for invalid inputs and division by zero (LBYL + EAFP)  
- Automation: GitHub Actions runs tests on each push; build fails if coverage < 100%  
- Documentation: This README provides setup, usage, structure, and testing guidance  
