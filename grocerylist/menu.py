class menu:
    def __init__(self):
        pass

    def show_menu(self):
        print("\n --Grocery List--")
        print("""
        1. Add Items,
        2. View Items,
        3. Remove Items,
        4. Total
        5. Discount
        6. Exit
        """)

    def user_input_choice(self):
        return input("Enter choice: ")
