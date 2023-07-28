# author: App05-Group84
#dev(s): @samrudhShetty
# creation date: 03/04/2023
# last modified: 05/05/2023
# description: create main, main_menu and generate_test_data methods

from user_admin import UserAdmin
from user_teacher import UserTeacher
from user_student import UserStudent
from user import User
from unit import Unit


def main_menu():
    #main menu function
    print("\nWelcome to the Student Information Management System!")
    print("Please choose an option:")
    print("1. Login")
    print("2. Exit")

def generate_test_date():
    #genearte test data function
    # admin = User("admin","password","AD","enrolled")
    admin = UserAdmin(user_name="admin", user_password="admin")

    # Three units data input
    units = {
        "FIT6060": Unit(unit_code="SAT2300", unit_name="Statistics1", unit_capacity=40),
        "FIT9090": Unit(unit_code="SAT2102", unit_name="Statistic modelling", unit_capacity=40),
        "FIT6556": Unit(unit_code="SAT1036", unit_name="Probability", unit_capacity=40)
    }

    # Three teachers data input
    teachers = {
        "teacher_1": UserTeacher(user_name="teacher1", user_password="teacher1", teach_units="(SAT2300),"),
        "teacher_2": UserTeacher(user_name="teacher2", user_password="teacher2", teach_units="(SAT2102),"),
        "teacher_3": UserTeacher(user_name="teacher3", user_password="teacher3", teach_units="(SAT1036),")
    }

    # Ten students data input
    students = {
        "student1": UserStudent(user_name="student1", user_password="pass1", enrolled_units="(SAT2300,21), (SAT1036,-1),"),
        "student2": UserStudent(user_name="student2", user_password="pass2", enrolled_units="(SAT2300,45), (SAT2102,34),"),
        "student3": UserStudent(user_name="student3", user_password="pass3", enrolled_units="(SAT2102,-1), (SAT1036,25),"),
        "student4": UserStudent(user_name="student4", user_password="pass4", enrolled_units="(SAT2102,78), (SAT2300,-1),"),
        "student5": UserStudent(user_name="student5", user_password="pass5", enrolled_units="(SAT1036,90), (SAT2102,45),"),
        "student6": UserStudent(user_name="student6", user_password="pass6", enrolled_units="(SAT2300,25), (SAT1036,-1),"),
        "student7": UserStudent(user_name="student7", user_password="pass7", enrolled_units="(SAT2102,45), (SAT2300,-1),"),
        "student8": UserStudent(user_name="student8", user_password="pass8", enrolled_units="(SAT2300,95), (SAT1036,-1),"),
        "student9": UserStudent(user_name="student9", user_password="pass9", enrolled_units="(SAT2102,45), (SAT1036,34),"),
        "student10": UserStudent(user_name="student10", user_password="pass10", enrolled_units="(SAT2300,78), (SAT2102,-1), (SAT1036,67),")
    }

    # putting test data to file
    with open("data/user.txt", "w+") as f:
        f.write(admin.__str__() + "\n")
        for teacher in teachers.values():
            f.write(teacher.__str__() )
        for student in students.values():
            f.write(student.__str__() + "\n")

    with open("data/unit.txt", "w+") as f:
        for unit in units.values():
            f.write(unit.__str__() + "\n")

def main():
    # calling test data geneartion function
    generate_test_date()
    # main menu function call
    main_menu()

    while True:
        try:
            user_choice = int(input("please enter your choice: "))
        # wrong user input check
        except ValueError:
            user_choice = 9

        # login
        if user_choice == 1:
            user_name = input("username: ")
            user_password = input("password: ")
            a = User()
            login_result = a.login(user_name, user_password)
            if login_result is None:
                print("Invalid username or password or deactivated")
                main_menu()
            else:
                while True:
                    u_data = login_result.strip().split(", ")
                    if u_data[3] == 'AD':
                        # Admin user block
                        t = UserAdmin()
                        t.admin_menu()
                        admin_choice = input("Your choice: ")
                        if admin_choice == "1":
                            # Search user information
                            user_name = input("Enter the username to search: ")
                            t.search_user(user_name)

                        elif admin_choice == "2":
                            # List all users' information
                            print("All users:")
                            t.list_all_users()

                        elif admin_choice == "3":
                            # List all units' information
                            print("All units:")
                            t.list_all_units()

                        elif admin_choice == "4":
                            # Enable/Disable user
                            user_name = input("Enter the username to enable/disable: ")
                            t.enable_disable_user(user_name)
                            # print(u_data[3])
                            # print("The new status of " +  + " is " +  + " .")

                        elif admin_choice == "5":
                            # Add user
                            user_type = input("Enter the role of user: ")
                            user_id = t.generate_user_id()
                            if user_type == 'TA':
                                user_test = UserTeacher(user_id=user_id, user_name=input("Input user name: "),user_role='TA')
                                t.add_user(user_test)
                            elif user_type == 'ST':
                                user_test = UserStudent(user_id=user_id, user_name=input("Input user name: "),user_role='ST')
                                t.add_user(user_test)
                            else:
                                print("Invalid user type.")

                            # print(u_data[3])
                            # print("The new status of " +  + " is " +  + " .")
                            main_menu()
                        #
                        elif admin_choice == "6":
                            # Delete user
                            user_name = input("Enter the username to be deleted:")
                            t.delete_user(user_name)
                            print("User deleted!")
                        elif admin_choice == "7":
                            print("You have logged out")
                            main_menu()
                            break
                        else:
                            # wrong input
                            print("Invalid choice. Please enter a valid choice.")
                    elif u_data[3] == 'TA':
                        # Teacher user block
                        teacher = UserTeacher(login_result)
                        t = UserTeacher()
                        t.teacher_menu()
                        teacher_choice = input("Your choice: ")
                        if teacher_choice == "1":
                            # listing units taught
                            print("All units taught by you:")
                            teacher.list_teach_units()

                        elif teacher_choice == "2":
                            # adding a new unit
                            print("Add new teaching unit")
                            uni_test = Unit(unit_code=input('Input code name: ')
                                            , unit_name=input('Input the unit name:'))
                            teacher.add_teach_unit(uni_test)

                        elif teacher_choice == "3":
                            # deleting the unit
                            unit_code = input("Enter the Unit code that you want to delete")
                            teacher.delete_teach_unit(unit_code)

                        elif teacher_choice == "4":
                            # listing all enrolled units
                            unit_code=input("Enter unit code to be checked:")
                            print("Listing all enrolled students")
                            teacher.list_enrol_students(unit_code)

                        elif teacher_choice == "5":
                            # showing max/min/avg score
                            unit_code =input("Enter Unit code to find the max/min/avg score")
                            teacher.show_unit_avg_max_min_score(unit_code)

                        elif teacher_choice == "6":
                            # Log out
                            print("You have logged out")
                            main_menu()
                            break
                        else:
                            print("Invalid choice. Please enter a valid choice.")

                    elif u_data[3] == 'ST':
                        # Student user block
                        student = UserStudent(login_result)
                        t = UserStudent()
                        t.student_menu()
                        student_choice = input('your choice:')
                        if student_choice == '1':
                            # listing all available units
                            print('All available units:')
                            student.list_available_units()

                        if student_choice == '2':
                            # lisitng all enrolled unit
                            print('Your enrolled units:')
                            student.list_enrolled_units()

                        if student_choice == '3':
                            # enrolling to unit
                            unit_code = input('Enter unit code you want to enrol in:')
                            unit_handle = open('data/unit.txt', 'r')
                            unit_string = unit_handle.read().strip()

                            if unit_code not in unit_string:
                                print(f'{unit_code} is not in unit list')
                            else:
                                student.enrol_unit(unit_code)

                            unit_handle.close()

                        if student_choice == '4':
                            # Dropping unit
                            unit_code = input('Enter unit code you want to drop:')
                            student.drop_unit(unit_code)

                        if student_choice == '5':
                            # checking score
                            unit_code = input('Input unit code to check score:')
                            student.check_score(unit_code)

                        if student_choice == '6':
                            # generating code
                            unit_code = input('Input unit code to generate score:')
                            student.generate_score(unit_code)

                        if student_choice == '7':
                            # Log out
                            print('You are logged out')
                            main_menu()
                            break

                        else:
                            print('\nPlease enter a number 1 to 7')

        elif user_choice == 2:
            # Log out
            print("Goodbye!")
            break

        else:
            print("\nplease enter a number 1 to 2")
            main_menu()

if __name__ == "__main__":
    main()
