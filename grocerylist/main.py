from menu import *
from grocery import *

budget = 0.0
items = {}
set_budget()

while True:
    show_menu()
    
    choice = user_input_choice()
    

    if choice == "1":
        add_items(items)
    elif choice == "2":
        view_items(items)
    elif choice == "3":
        remove_items(items)
    elif choice == "4":
        calculate_total(items)
    elif choice == "5":
        apply_discount(items)
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again")