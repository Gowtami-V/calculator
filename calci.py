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

    def power(self, x, y):
        return x ** y
    
    def square_root(self, x):
        if x < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return x ** 0.5
    
    def percentage(self, x):
        return x / 100
    
    def factorial(self, x):
        if not isinstance(x, int):
            raise ValueError("Factorial only works with integers")
        if x < 0:
            raise ValueError("Factorial of negative number is undefined")
        if x == 0:
            return 1
        return x * self.factorial(x - 1)

if __name__ == "__main__":
    calc = Calculator()
    print("Basic operations:")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"2 * 6 = {calc.multiply(2, 6)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    
    print("\nAdvanced operations:")
    print(f"2^3 = {calc.power(2, 3)}")
    print(f"√16 = {calc.square_root(16)}")
   
