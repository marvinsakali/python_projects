class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


def main():
    student = get_student()
    
    print(f'{student.name} is from {student.house}')


def get_student():
    name = input("Enter students name: ")
    house = input("Enter students home: ")
    return Student(name, house)
    

if __name__ == "__main__":
    main()

