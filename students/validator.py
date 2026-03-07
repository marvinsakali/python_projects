def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Enter a value(integer)")


def get_no_empty(prompt):
    while True:        
        try:
            value = input(prompt).strip()
            return value
        except ValueError:
            print("Input can not be empty!")


def get_year(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 1 <= 5:
                return value
            else:
                print('Enter the year')
        except ValueError:
            print("Invalid input")
