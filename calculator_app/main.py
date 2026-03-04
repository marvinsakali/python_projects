import menu
import calculator


def main():
    calc = calculator.calculator()
    while True:
        mnu = menu.menu()
        mnu.show_menu()
        choice = mnu.user_input()

        if choice == 1:
            calc.square()
        elif choice == 2:
            calc.add()
        elif choice == 3:
            calc.subtract()
        elif choice == 4:
            calc.multiply()
        elif choice == 5:
            calc.divide()
        elif choice == 6:
            print('Exiting...')
            break
        else:
            print('Invalid! Try Again!')


if __name__ == "__main__":
    main()
