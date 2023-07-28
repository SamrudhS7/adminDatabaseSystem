# author: App05-Group84
#dev(s): @yuxiangZou; @davidChong; @samrudhShetty
# creation date: 24/04/2023
# last modified: 05/05/2023
# description: create Unit subclass and related methods

import random

class Unit:
    """
           Initializes a Unit object with the given parameters.
           :param unit_id: (int) The ID of the unit. If None, generates a random 7-digit ID.
           :param unit_code: (str) The code of the unit.
           :param unit_name: (str) The name of the unit.
           :param unit_capacity: (int) The maximum capacity of the unit.
    """
    def __init__(self, unit_id=None, unit_code='', unit_name='', unit_capacity=40):
        """
               Initializes a Unit object with the given parameters.
               :param unit_id: (int) The ID of the unit. If None, generates a random 7-digit ID.
               :param unit_code: (str) The code of the unit.
               :param unit_name: (str) The name of the unit.
               :param unit_capacity: (int) The maximum capacity of the unit.
        """
        self.unit_id = unit_id if unit_id is not None else self.generate_unit_id()
        self.unit_code = unit_code
        self.unit_name = unit_name
        self.unit_capacity = unit_capacity

    def __str__(self):
        """
                Returns a string representation of the Unit object.
                :return: (str) The string representation of the Unit object.
        """
        return f"{self.unit_id}, {self.unit_code}, {self.unit_name}, {self.unit_capacity}"


    def generate_unit_id(self):
        """
        Generates a random 7-digit ID for the unit.
        :return: (int) The generated ID.
        """
        # generating random unit id number
        return random.randint(1000000, 9999999)
