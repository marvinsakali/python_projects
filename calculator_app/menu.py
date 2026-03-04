
class menu:
    def user_input(self):
        return int(input('Enter your choice: '))

    def show_menu(self):
        print("\n****** Calculator ******")
        print('Menu')
        print(
            "1. square\n"
            "2. Add\n"
            "3. Subtract\n"
            "4. Multiply \n"
            "5. Divide\n"
            "6. Exit"
        )
