def main():
    name = input("What is your name? ")
    print(greeting(name))


def greeting(to="World"):
    return f"Hello, {to}"

if __name__ == "__main__":
    main()
