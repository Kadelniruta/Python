class Calculator:
    def add(self, a, b):
        """Return the sum of two numbers."""
        return a + b

    def subtract(self, a, b):
        """Return the difference of two numbers."""
        return a - b

    def multiply(self, a, b):
        """Return the product of two numbers."""
        return a * b

    def divide(self, a, b):
        """Return the quotient of two numbers, handling division by zero."""
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b


# Testing the Calculator class
calculator = Calculator()



    # Test addition
print("Addition (5 + 3):", calculator.add(5, 3))

    # Test subtraction
print("Subtraction (5 - 3):", calculator.subtract(5, 3))

    # Test multiplication
print("Multiplication (5 * 3):", calculator.multiply(5, 3))

    # Test division
print("Division (5 / 3):", calculator.divide(5, 3))
print("Division (5 / 0):", calculator.divide(5, 0))