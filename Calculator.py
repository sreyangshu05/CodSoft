class SimpleCalculator:
    def __init__(self):
        self.result = None
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    def calculate(self, a, b, operation):
        try:
            if operation == '+':
                self.result = self.add(a, b)
            elif operation == '-':
                self.result = self.subtract(a, b)
            elif operation == '*':
                self.result = self.multiply(a, b)
            elif operation == '/':
                self.result = self.divide(a, b)
            else:
                raise ValueError("Invalid operation.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except ZeroDivisionError as zde:
            print(f"Error: {zde}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            if self.result is not None:
                print(f"The previous result of {a} {operation} {b} is {self.result}")
            else:
                print("Calculation could not be completed.")
def main():
    calc = SimpleCalculator()
    while True:
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            operation = input("Enter the operation (+, -, *, /): ")
            calc.calculate(a, b, operation)
        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(f"Unexpected input error: {e}")
        choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Exiting the calculator. Goodbye!")
            break
if __name__ == "__main__":
    main()
