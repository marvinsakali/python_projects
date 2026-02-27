# Object Oriented programming
# Creating a sample class of empoloyees in a company

class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = (first + "." + last + "@jorajoh.com").lower()

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developers(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, language):
        super().__init__(first, last, pay)
        self.language = language


class Managers(Employee):
    raise_amount = 1.15

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emps(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emps(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def show_employees(self):
        for i, emp in enumerate(self.employees):
            return (f"{i+1.} --> {emp.full_name()}")


dev1 = Developers('Marvin', 'Sakali', 50000, 'python')
mgn1 = Managers('Givens', 'Ogajo', 100000, [dev1])
print(dev1.language)
print(mgn1.email)
print(dev1.pay)
dev1.apply_raise()
print(mgn1.pay)
print(mgn1.show_employees())
