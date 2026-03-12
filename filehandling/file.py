import os
import csv


def create_user_dict(name, user_id):
    return {"name": name, "id": user_id}


def user_exists(user_id):
    if not os.path.exists("users.csv"):
        return False

    with open("users.csv", "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if int(row["id"]) == user_id:
                return True

    return False


def create_user():
    name = input("Enter name: ")
    user_id = int(input("Enter user_id: "))

    if user_exists(user_id):
        print("User Already exists")
        return

    file_exists = os.path.exists('users.csv')

    with open("users.csv", 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "id"])

        if not file_exists:
            writer.writeheader()

        writer.writerow(create_user_dict(name, user_id))

    print("User added successfully!")


create_user()
