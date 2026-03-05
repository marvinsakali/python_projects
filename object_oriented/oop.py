# Object Oriented programming
# Creating a sample class of empoloyees in a company
# import datetime


class Employee:
    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_employees += 1

    @property
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return ("{}.{}@company.com").format(self.first, self.last)

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @classmethod
    def set_raise_amount(cls, amt):
        cls.raise_amount = amt

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def from_string(cls, data_str):
        first, last, pay = data_str.split("-")
        return cls(first, last, int(pay))

    @staticmethod
    def work_day(day):
        if day.weekday() < 5:
            print(f'{day} is working day')
        else:
            return


class Developers(Employee):
    def __init__(self, first, last, pay, language):
        super().__init__(first, last, pay)
        self.language = language

    @classmethod
    def set_raise_amount(cls, amt):
        return super().set_raise_amount(amt)


class Managers(Employee):
    raise_amount = 1.15

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    @classmethod
    def set_raise_amount(cls, amt):
        return super().set_raise_amount(amt)

    def add_emps(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emps(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def show_employees(self):
        for i, emp in enumerate(self.employees):
            return (f"{i+1.} --> {emp.full_name()}")


emp1 = Employee('Mercy', 'Wekesa', 50000)
# dev1 = Developers('Marvin', 'Sakali', 50000, 'python')
# mgn1 = Managers('Givens', 'Ogajo', 100000, [dev1])
# emp3 = Employee.from_string('Val-Wekesa-50000')
# # Employee.full_name = 'Margaret Sakali'
# print(emp3.full_name)
# print(emp3.email)


# if __name__ == "__main__":
#     main()
