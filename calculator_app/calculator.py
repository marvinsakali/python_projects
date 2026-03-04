class calculator:
    def __init__(self):
        pass

    def square(self):
        n = int(input("Enter no: "))
        results = n ** 2
        print(f"The square of n is: {results}")
        return results

    def get_two_nos(self):
        x = int(input('Enter first no: '))
        y = int(input("Enter second no: "))
        return x, y

    def add(self):
        x, y = self.__init__get_two_nos()
        results = x + y
        print(f"{results}")
        return results

    def subtract(self):
        x, y = self.get_two_nos()
        results = x - y
        print(f"{results}")
        return results

    def multiply(self):
        x, y = self.get_two_nos()
        results = x * y
        print(f"{results}")
        return results

    def divide(self):
        x, y = self.get_two_nos()
        if y == 0:
            raise ZeroDivisionError("Cannot divide by 0")
        results = x / y
        print(f"{results}")
        return results
