import random


class Die:
    """Represent a die with the number of sides."""
    def __init__(self, number_of_sides):
        """Create a Die object """
        self.face_value = 1
        self.number_of_sides = number_of_sides

    def get_face_value(self):
        """Return the face value of the die"""
        return self.face_value

    def set_size(self, new_size):
        """Set the new size of the die"""
        if new_size > 0:
            self.number_of_sides = new_size

    def roll_die(self):
        """Roll the die and print the face value"""
        self.face_value = random.randint(1, self.number_of_sides)
        return self.get_face_value()


def main():
    """
    Drive the example.
    """
    die = Die(6)
    for _ in range(20):
        die.roll_die()


if __name__ == '__main__':
    main()
