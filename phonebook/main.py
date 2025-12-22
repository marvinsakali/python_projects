from menu import *
from contacts import *

contacts = []
names = set()

def main():

    while True:
        show_menu()
        choice = user_input_choice()

        if choice == "1":
            add_contacts(contacts, names)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            delete_contacts(contacts)
        elif choice == "4":
            search_contacts(contacts)
        elif choice == "5":
            print("Exiting... ")
            break

        else:
            print("Invalid choice. Try again")

main()
