from students import Students
from uni import University
import validator


def main():
    def show_menu():
        print("\n--- MENU ---")
        print(
            "1. Add Student\n"
            "2. Remove Student\n"
            "3. Display Student\n"
            "4. Register Course\n"
            "5. Exit"
        )
    uni = University()
    while True:
        show_menu()
        choice = validator.get_int("Enter your choice: ")
        
        if choice == 1:
            first = validator.get_no_empty("Enter first name: ")
            middle = validator.get_no_empty("Enter first middle: ")
            last = validator.get_no_empty("Enter last name: ")
            program = validator.get_no_empty("Enter program: ")
            year = validator.get_year("Enter the year of study: ")
            reg = validator.get_no_empty("Enter regestration no: ")

            student = Students(first, middle, last, reg, program, year)
            uni.add_student(student)

        elif choice == 2:
            student = validator.get_no_empty("Enter reg no: ")
            uni.remove_student(student)

        elif choice == 3:
            student_reg = validator.get_no_empty("Enter reg no: ")
            uni.display_student(student_reg)

        elif choice == 4:
            value = input("Enter reg no: ")
            unit = input("Enter the unit to register: ")
            uni.register_to_units(value, unit)

        elif choice == 5:
            print('Exiting..')
            break
        else:
            print("Invalid input")


if __name__ == '__main__':
    main()
