import os
import csv


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def create_user_dict(self):
        return {"name": self.name, "id": self.user_id}


class UserManager:
    def __init__(self):
        self.file = "users.csv"

    def user_exists(self, user_id):
        self.user_id = user_id
        if os.path.exists(self.file):
            with open(self.file, 'r') as f:
                reader = csv.DictReader(f)

                for row in reader:
                    if int(row['id']) == self.user_id:
                        print("User already exists!")
                        return True
        return False

    def create_user(self):
        self.name = input("Enter name: ")
        self.user_id = int(input("Enter id: "))

        user = User(self.name, self.user_id)

        file_exists = os.path.exists(self.file)

        if self.user_exists(self.user_id):
            return True

        with open(self.file, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['name', 'id'])

            if not file_exists:
                writer.writeheader()
            writer.writerow(user.create_user_dict())
        print("User added succesfuly!")

    def view_users(self):
        if os.path.exists(self.file):

            with open(self.file, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    name = row["name"]
                    id = row["id"]
                    print(f"{name} {id}")
                return True
        else:
            print("No users Found!")
            return False

    def delete_user(self, user_id):
        rows = []
        if not self.user_exists(user_id):
            print("User not found!")

        if os.path.exists(self.file):
            with open(self.file) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if int(row["id"]) != user_id:
                        rows.append(row)
            print(rows)

            with open(self.file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=["name", "id"])
                writer.writeheader()
                writer.writerows(rows)
            print("User deleted successfuly")

    def update_name(self, new_name):
        rows = []
        self.user_id = int(input("Enter user_id: "))
        if not self.user_exists(self.user_id):
            print("User not found!")
        with open(self.file, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                if int(row["id"]) == self.user_id:
                    row["name"] = new_name
                    rows.append(row)

        with open(self.file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['name', 'id'])
            writer.writeheader()
            writer.writerows(rows)
        print(f"User {self.user_id} succefully updated")


manage = UserManager()
manage.update_name('Ogajo Sakali')
# manage.delete_user(3)
