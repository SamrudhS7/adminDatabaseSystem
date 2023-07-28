# author: App05-Group84
#dev(s): @samrudhShetty
# creation date: 24/04/2023
# last modified: 05/05/2023
# description: create User subclass and related methods

import random


class User:
    """
    Initializes a new User object.

    Args:
        user_id (int): The user ID.
        user_name (str): The user name.
        user_password (str): The user password.
        user_role (str): The user role (default is 'ST').
        user_status (str): The user status (default is 'disabled').

    Returns:
        None.
    """
    def __init__(self, user_id=None, user_name=None, user_password=None, user_role='ST', user_status='disabled'):
        self.user_id = user_id if user_id is not None else self.generate_user_id()
        self.user_name = user_name
        self.user_password = self.encrypt(user_password) if user_password is not None else None
        self.user_role = user_role
        self.user_status = user_status

    def __str__(self):
        """
        Returns a string representation of the User object.

        Args:
            None.

        Returns:
            str: A string representation of the User object.
        """
        return f"{self.user_id}, {self.user_name}, {self.user_password}, {self.user_role}, {self.user_status}"

    def generate_user_id(self):
        """
        Generates a random 5-digit user ID.

        Args:
            None.

        Returns:
            int: A random 5-digit user ID.
        """
        #is it seq or random?
        return random.randint(10000, 99999)

    def check_username_exist(self, user_name):
        """
        Checks if a user with the given user name exists in the user.txt file.

        Args:
            user_name (str): The user name to search for.

        Returns:
            bool: True if the user exists, False otherwise.
        """
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
        # Return True if it exists, False otherwise
        return False

    def encrypt(self, user_password):
        """
        Encrypts a given user password using a custom encryption algorithm.

        Args:
            user_password (str): The password to encrypt.

        Returns:
            str: The encrypted password.
        """
        str_1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        str_2 = "!#$%&()*+-./:;<=>?@\^_`{|}~"
        encrypted_password = "^^^"
        for letter in user_password:
            ascii_code = ord(letter)
            str_1_index = ascii_code % len(str_1)
            str_2_index = user_password.index(letter) % len(str_2)
            encrypted_password += str_1[str_1_index] + str_2[str_2_index]

        encrypted_password += "$$$"
        return encrypted_password
    #print(encrypt('password')

    def login(self, user_name, user_password):
        """
        Logs in a user with the given user name and password.

        Args:
            user_name (str): The user name to login with.
            user_password (str): The password to login with.

        Returns:
            str or None: The user data from the user.txt file if the login is successful, None otherwise.
        """

        with open("data/user.txt", "r") as f:
            for line in f:
                u_data = line.strip().split(", ")
                if len(u_data) >= 5:
                    try:
                        u_data[4] = u_data[4].replace(',', '')
                    except:
                        pass
                    if user_name == u_data[1] and self.encrypt(user_password) == u_data[2] and u_data[4] == 'enabled':
                        return line
            return None












#test snippets
# print(admin_test)
# admin_test="pass"
# a=User()
# ad=a.encrypt(admin_test)
# print(ad)



# pass
