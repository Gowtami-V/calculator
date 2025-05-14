class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

if __name__ == "__main__":
    calc = Calculator()
    print(calc.add(5, 3))
    print(calc.subtract(10, 4))
    print(calc.multiply(2, 6))
    print(calc.divide(15, 3))
