# adminDatabaseSystem
An elementary educational administration database system commonly utilized in schools.
This project involves creating a Python program that simulates an educational administration system. The program caters to three types of users: administrators, teachers, and students. Each user can access specific functions by logging into the system and can log out to return to the main menu for re-login or program exit. The program will run continuously until the user chooses to quit.

Users can log in with different account types and utilize corresponding system functions based on their roles. The following provides a brief overview of the available system functions for each user type:

Admin:

Administrators can manage user and unit information.
They can search and display specific user information as needed.
The administrator can view all user and unit information stored in the system.
Additionally, administrators can update user statuses, enabling or disabling their accounts.
They have the privilege to add and delete users.
Teacher:

Teachers can log in and perform actions such as adding and deleting teaching units.
They can access information about all teaching units available.
Teachers can view a list of all registered students.
The system also displays the average, highest, and lowest scores for each unit.
Student:

Students, upon login, have various options available.
They can view all units available for enrollment.
Students can check the units they are already enrolled in.
They can choose to enroll or drop units.
The system allows students to check their marks for enrolled units and generate new marks for the units, adding them to the list.
Implementation:
To implement the program, we have created five classes, each defined in separate Python files. The main Python file, main.py, serves as the program execution file and the menu driver for the classes. Here is an overview of the classes:

Unit: Defines properties of a unit, including unit ID, unit code, unit name, and registration capacity.
User: Defines attributes of login users, including name, password, user type, and login status.
User_Admin: A subclass of User that specifies attributes for administrators, including their level of access to user and unit management functions.
User_Teacher: A subclass of User that specifies attributes for teachers, including the units they teach.
User_Student: A subclass of User that specifies attributes for students, such as the units they are enrolled in and their scores.
These classes work together in the main.py file, ensuring seamless execution of the program and enabling the utilization of all functionalities within the menu system.
