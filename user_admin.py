# author: App05-Group84
#dev(s): @samrudhShetty
# creation date: 24/04/2023
# last modified: 05/05/2023
# description: create UserAdmin subclass and related methods

from user import User
from user_student import UserStudent
from user_teacher import UserTeacher


class UserAdmin(User):
    """
    A class representing a user with administrative privileges.
    Inherits from the User class.

    Methods:
    - __init__: initializes UserAdmin instance with user_id, user_name, user_password, user_role, user_status
    - __str__: returns string representation of UserAdmin instance
    - admin_menu: prints list of operations that can only be performed by an admin
    - search_user: searches for user by user_name in user.txt and prints the required user's information
    - list_all_users: prints a list of all users and their information from user.txt
    - list_all_units: prints a list of all units and their information from unit.txt
    - enable_disable_user: enables/disables user by user_name in user.txt
    - add_user: adds a UserTeacher or UserStudent instance to user.txt
    - delete_user: deletes user by user_name from user.txt
    """
    def __init__(self, user_id=0, user_name='', user_password='', user_role='AD', user_status='enabled'):
        super().__init__(user_id, user_name, user_password, user_role, user_status)

    def __str__(self):
        # Returns string representation of UserAdmin instance.
        return super().__str__()

    def admin_menu(self):
        # Prints list of operations that can only be performed by an admin.
        print("List of operations that can only be performed by an admin:")
        print("1. Search user")
        print("2. List all users")
        print("3. List all units")
        print("4. Enable/disable user")
        print("5. Add user")
        print("6. Delete user")
        print("7. Logout")

    def search_user(self, user_name):
        # Searches for user by user_name in user.txt and prints the required user's information.
        # If user is not found, prints "User not found.".
        found_name = False
        with open("data/user.txt", "r") as file:
            for line in file:
                u_data = line.strip().split(", ")
                if u_data[1] == user_name:
                    print(f"Required user: {line}")
                    found_name = True
                    break
        if not found_name:
            print("User not found.")

    def list_all_users(self):
        # Prints a list of all users and their information from user.txt.
        print("List of all users:")
        with open("data/user.txt", "r") as file:
            for line in file:
                print(line)

    def list_all_units(self):
        # Prints a list of all units and their information from unit.txt.
        print("List of all units:")
        with open("data/user.txt", "r") as file:
            for line in file:
                print(line)

    def enable_disable_user(self, user_name):
        # Enables/disables user by user_name in user.txt.
        # If user is not found, prints "User not found.".
        found_line = False
        with open("data/user.txt", "r") as file:
            data = file.readlines()
        with open("data/user.txt", "w") as file:
            for line in data:
                # change delimiter when decided
                user_data = line.strip().split(", ")
                if user_data[1] == user_name:
                    if user_data[4] == "enabled":
                        user_data[4] = "disabled"
                    else:
                        user_data[4] = "enabled"
                    # file.seek(0)
                    file.write(", ".join(user_data) + "\n")
                    #file.truncate()
                    found_line = True
                else:
                    file.write(line)
        if not found_line:
            print("User not found.")

    def add_user(self,user_obj:UserTeacher or UserStudent):
        # adds user by user_obj in user.txt.
        user_obj.user_password==self.encrypt(user_obj.user_password)
        with open("data/user.txt", "a") as file:
            file.write(str(user_obj) + "\n")
            print("User", user_obj.user_name, "added successfully.")

    def delete_user(self, user_name):
        #deletes user by user_name in user.txt
        found = False
        with open("data/user.txt", "r") as file:
            data = file.readlines()
        with open("data/user.txt", "w") as file:
            for line in data:
                user_data = line.strip().split(", ")
                if user_data[1] == user_name:
                    found = True
                else:
                    file.write(line)
        if not found:
            print("User not found.")

    # pass

