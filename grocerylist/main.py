import menu
import grocery

budget = 0.0
items = {}
groc = grocery.grocery()
groc.set_budget()
mnu = menu.menu()

while True:
    mnu.show_menu()
    choice = mnu.user_input_choice()

    if choice == "1":
        groc.add_items(items)
    elif choice == "2":
        groc.view_items(items)
    elif choice == "3":
        groc.remove_items(items)
    elif choice == "4":
        groc.calculate_total(items)
    elif choice == "5":
        groc.apply_discount(items)
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again")
