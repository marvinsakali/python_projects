from Menu import *
from tasks import *

tasks = []


def main():

    while True:
        show_menu()
        choice = get_user_input()

        if choice == 1:
            add_tasks(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice== 3:
            complete_tasks(tasks)
        elif choice == 4:
            delete_tasks(tasks)
        elif choice == 5:
            print("Goodbye!")
            break
        else: 
            print("Invalid choice.Try again!")
main()





