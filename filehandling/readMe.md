User Management System

A simple Python-based User Management System that allows you to create, view, update, and delete users using a CSV file for storage. Each user is represented with a name and a unique ID.

Features

Add a new user
Users can be added with a name and unique ID. The system prevents duplicate IDs.

View all users
Displays all users stored in the CSV file.

Update user name
Allows updating a user's name using their unique ID.

Delete a user
Deletes a user based on their ID.

Persistent storage
Users are stored in users.csv, ensuring data persists across sessions.

Classes
User

Represents an individual user.

Attributes:

name – Name of the user.

user_id – Unique ID of the user.

Methods:

create_user_dict() – Returns a dictionary representation of the user.

UserManager

Handles all user management operations and interacts with the CSV file.

Methods:

user_exists(user_id) – Checks if a user already exists in the CSV.

create_user() – Prompts for user details and adds them to the CSV.

view_users() – Prints all users from the CSV.

delete_user(user_id) – Deletes a user with the specified ID.

update_name(new_name) – Updates a user's name using their ID.