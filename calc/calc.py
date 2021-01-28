
class Calc:

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        try:
            x / y
        except ZeroDivisionError:
            print("You can't divide by zero.")
        return x / y
