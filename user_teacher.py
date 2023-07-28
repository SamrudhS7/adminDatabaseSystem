# author: App05-Group84
#dev(s): @samrudhShetty
# creation date: 24/04/2023
# last modified: 05/05/2023
# description: create UserTeacher subclass and related methods

import re
from user import User
from unit import Unit

# define UserTeacher class and constructor inheriting attributes from User class
class UserTeacher(User):
    def __init__(self, user_id=None, user_name='teacher', user_password='teacher', user_role='TA',
                 user_status='enabled', teach_units=""):
        self.teach_units = teach_units
        super().__init__(user_id, user_name, user_password, user_role, user_status)

    def __str__(self) -> str:
        return f'{self.user_id}, {self.user_name}, {self.user_password}, {self.user_role}, {self.user_status}, ' \
               f'{self.teach_units}\n'

    # display menu of options that student can choose
    def teacher_menu(self):
        print("""
        Teacher Menu Options:
        1. List Teaching Unit
        2. Add Teaching Unit
        3. Delete Teaching Unit
        4. List Enrol Students
        5. Show Unit Statistics Score (mean, max, min)
        6. Logout
         """)

    # display units which teacher is teaching
    def list_teach_units(self):
        user_handle = open('data/user.txt', 'r')

        # search txt file for matching user id and units
        for line in user_handle:
            if str(self.user_id) in line:
                line_list = line.split(',', 5)
                self.teach_units = line_list[5].strip()
                print(self.teach_units)

        if self.teach_units == "":
            print('you are currently not teaching any units')

        user_handle.close()

    # enables a teacher to add unit to unit list and user list
    def add_teach_unit(self, unit_obj):
        # saves the new unit to unit.txt
        unit_handle = open('data/unit.txt', 'r+')
        unit_string = unit_handle.read().strip()
        # search file to check if unit already exists
        if str(unit_obj.unit_id) in unit_string:
            print(f'{unit_obj.unit_code} already exists in unit list')
        else:
            # add new unit and rewrite file
            unit_string = unit_string + f"\n{unit_obj}"
            unit_handle.seek(0)
            unit_handle.write(unit_string)
            print(f'{unit_obj.unit_code} added to unit list')

        unit_handle.close()

        # save the unit code of the new unit associated with the teacher to user.txt
        user_handle = open('data/user.txt', 'r+')
        user_lines = user_handle.readlines()
        # remove any items in list which are just an empty line
        try:
            user_lines.remove("\n")
        except:
            pass

        # search list of lines for matching user ID
        for line in user_lines:
            if str(self.user_id) in line:
                if str(unit_obj.unit_code) in line:
                    print(f'you are already teaching {unit_obj.unit_code}')
                # check number of units
                else:
                    # replace existing line with new line including new unit
                    index = user_lines.index(line)
                    new_line = line.replace(line, line.strip() + f' ({unit_obj.unit_code}),\n')
                    user_lines[index] = new_line
                    print(f'you are now teaching {unit_obj.unit_code}')
                    # rewrite txt file using list of modified lines
                    user_handle.seek(0)
                    for line in user_lines:
                        user_handle.write(line)
                        user_handle.truncate()

        # update teach_units attribute
        for line in user_handle:
            if str(self.user_id) in line:
                line_list = line.split(',', 5)
                self.teach_units = line_list[5].strip()

        user_handle.close()

    # remove a unit from unit list and teaching list
    def delete_teach_unit(self, unit_code):
        # check if unit is not in unit list
        unit_handle = open('data/unit.txt', 'r')
        unit_string = unit_handle.read().strip()

        if unit_code not in unit_string:
            print(f'{unit_code} is not in unit list')

        unit_handle.close()

        # delete unit from unit.txt
        unit_handle = open('data/unit.txt', 'r+')
        unit_lines = unit_handle.readlines()
        # remove any items in list which are just an empty line
        try:
            unit_lines.remove('\n')
        except:
            pass

        for line in unit_lines:
            if unit_code in line:
                index = unit_lines.index(line)
                del unit_lines[index]
                print(f'{unit_code} dropped from unit list')
                # rewrite txt file using list of modified lines
                unit_handle.seek(0)
                for line in unit_lines:
                    unit_handle.write(line)
                    unit_handle.truncate()

        unit_handle.close()

        # check if unit is not in user list
        user_handle = open('data/user.txt', 'r')
        user_string = user_handle.read().strip()

        if unit_code not in user_string:
            print(f'{unit_code} is not taught or enrolled in user list')

        user_handle.close()

        # remove unit from teacher and students in user list
        user_handle = open('data/user.txt', 'r+')
        user_lines = user_handle.readlines()
        # remove any items in list which are just an empty line
        try:
            user_lines.remove('\n')
        except:
            pass

        # search list of lines for matching unit ID
        for line in user_lines:
            if unit_code in line:
                # replace existing line with new line excluding dropped unit
                index = user_lines.index(line)
                new_line = re.sub(f' \({unit_code}.*?\),', '', line)
                user_lines[index] = new_line
                print(f'one instance (teaching/enrolment) of {unit_code} removed from user file')
        # rewrite txt file using list of modified lines
        user_handle.seek(0)
        for line in user_lines:
            user_handle.write(line)
            user_handle.truncate()

        # update teach_units attribute
        for line in user_handle:
            if str(self.user_id) in line:
                line_list = line.split(',', 5)
                self.teach_units = line_list[5].strip()

        user_handle.close()

    # lists details of all students enrolled in a unit code
    def list_enrol_students(self, unit_code):
        # find and print lines of students enrolled in unit code
        user_handle = open('data/user.txt', 'r')
        user_lines = user_handle.readlines()

        student_counter = 0

        for line in user_lines:
            if unit_code in line and "ST" in line:
                print(line.strip())
                student_counter += 1

        if student_counter == 0:
            print(f'there are no students enrolled in {unit_code}')

        user_handle.close()

    # display the unit’s average, maximum and minimum score
    def show_unit_avg_max_min_score(self, unit_code):
        with open('data/user.txt', 'r') as user_handle:
            user_lines = user_handle.readlines()

        # remove any items in list which are just an empty line
        user_lines = [line.strip() for line in user_lines if line.strip()]

        integer_list = []

        # find all students enrolled in unit code and change unit score to integer
        for line in user_lines:
            if unit_code in line and "ST" in line:
                unit_tuple = str(re.findall(f'{unit_code}..\d*', line))
                unit_int_step1 = re.sub(f"\['{unit_code},", '', unit_tuple)
                unit_int_step2 = re.sub(f"'\]", '', unit_int_step1)
                unit_integer = int(unit_int_step2)
                integer_list.append(unit_integer)

        try:
            unit_avg = round(sum(integer_list) / len(integer_list), 2)
            unit_max = max(integer_list)
            unit_min = min(integer_list)
            print(f'{unit_code} - average score = {unit_avg}, unit max = {unit_max}, unit min = {unit_min}')
        except ZeroDivisionError:
            print(f'Cannot show {unit_code} statistics because no students enrolled')

        user_handle.close()
