import random


class Die:

    def __init__(self, number_of_sides):
        self.face_value = 1
        self.number_of_sides = number_of_sides

    def get_face_value(self):
        print(self.face_value)

    def set_size(self, new_size):
        if new_size > 0:
            self.number_of_sides = new_size

    def roll_die(self):
        self.face_value = random.randint(1, self.number_of_sides)
        return self.get_face_value()
