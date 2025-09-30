from app.operation import Operations

class Calculation:
    def __init__(self, operation, a, b):
        self.operation = operation
        self.a = a
        self.b = b

    def perform(self):
        return self.operation(self.a, self.b)

    def __str__(self):
        return f"{self.a} {self.operation.__name__} {self.b} = {self.perform()}"

class CalculationFactory:
    @staticmethod
    def create(op, a, b):
        if op == "add": return Calculation(Operations.add, a, b)
        if op == "subtract": return Calculation(Operations.subtract, a, b)
        if op == "multiply": return Calculation(Operations.multiply, a, b)
        if op == "divide": return Calculation(Operations.divide, a, b)
        raise ValueError(f"Unknown operation: {op}")

class CalculationHistory:
    history = []

    @classmethod
    def add(cls, calculation):
        cls.history.append(calculation)
