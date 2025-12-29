def main():
    
    x= user_input()
    print(f"{x} squared is {square(x)}")

def square(n):
    return n * n
def user_input():
    return int(input("What's your number?"))
    

if __name__ == "__main__":
    main()