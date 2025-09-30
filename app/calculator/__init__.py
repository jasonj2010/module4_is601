from app.operation import Operations
from app.calculation import CalculationFactory, CalculationHistory

def calculator():
    print("Welcome to the calculator REPL! Type 'help' for commands or 'exit' to quit")

    while True:
        user_input = input("Enter command: ").strip().lower()
        if user_input == "exit":
            print("Goodbye!")
            break
        elif user_input == "help":
            print("Commands: add, subtract, multiply, divide, history, exit")
            continue
        elif user_input == "history":
            for calc in CalculationHistory.history:
                print(calc)
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            calc = CalculationFactory.create(user_input, a, b)
            result = calc.perform()
            print(f"Result: {result}")
            CalculationHistory.add(calc)
        except ValueError as e:
            print(f"Error: {e}")
        except Exception:
            print("Invalid command. Type 'help' for options.")
