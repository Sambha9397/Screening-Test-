# Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def calculate(self):
        match self.operation:
            case "add":
                return self.a + self.b
            case "subtract":
                return self.a - self.b
            case "multiply":
                return self.a * self.b
            case "divide":
                if self.b == 0:
                    return "Error: Division by zero"
                return self.a / self.b
            case _:
                return "Invalid operation"


calc1 = Calculator(10.0, 20.0, "divide")
result = calc1.calculate()
print(result)
