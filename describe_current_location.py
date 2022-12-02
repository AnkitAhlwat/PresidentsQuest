import json
from combat import setup_combat
from get_user_choice import get_user_choice
from die import Die


def display_map():
    with open("coordinates.json") as file_object:
        coordinates = json.load(file_object)
    print("Current map")

    with open("character.json","r") as file_object:
        character_dictionary = json.load(file_object)
        if character_dictionary["Icons"] == "cmd":
            end_string = ""
        else:
            end_string = "`"

    position = 0
    for room, icons in coordinates.items():
        print(icons, end=end_string)
        position += 1
        if position == 8:
            print()
            position = 0

def check_for_random_enemy():
    current_die = Die(10)
    dice_roll = current_die.roll_die()
    if dice_roll <= 2:
        print("A random enemy politician!")
        setup_combat()
        find_current_location()


def is_valid_move(current_location):
    with open("coordinates.json", "r") as file_object:
        coordinates = json.load(file_object)
        if current_location not in coordinates or coordinates[current_location] == "⬛":
            return False
        return True

def update_current_location(y_coordinate, x_coordinate, direction):
    y_map = {"North": -1, "South": +1, "West": 0, "East": 0}
    x_map = {"West": -1, "East": +1, "North": 0, "South": 0}
    with open("coordinates.json", "r") as file_object:
        coordinates = json.load(file_object)
    if is_valid_move(f'{y_coordinate + y_map[direction]}:{x_coordinate + x_map[direction]}'):
        y_coordinate += y_map[direction]
        x_coordinate += x_map[direction]
        with open("character.json", "r") as file_object:
            character_dictionary = json.load(file_object)
            coordinates[f'{character_dictionary["Y-coordinate"]}:{character_dictionary["X-coordinate"]}'] = "[ ]"
            character_dictionary["Y-coordinate"] = y_coordinate
            character_dictionary["X-coordinate"] = x_coordinate
            coordinates[f'{character_dictionary["Y-coordinate"]}:{character_dictionary["X-coordinate"]}'] = "[X]"
        with open("character.json", "w") as file_object:
            json.dump(character_dictionary, file_object)
        with open("coordinates.json", "w") as file_object:
            json.dump(coordinates, file_object)
        describe_current_location(y_coordinate, x_coordinate)

    else:
        print("That is not a valid move try again")
        describe_current_location(y_coordinate, x_coordinate)


def describe_current_location(y_coordinate, x_coordinate):
    display_map()
    with open("white_house_room_descriptions.json", "r") as file_object:
        room_description_dictionary = json.load(file_object)
        print(room_description_dictionary[f'{y_coordinate}:{x_coordinate}'])
    check_for_random_enemy()
    direction = get_user_choice("Decision", "Where would you like to go", ["North", "East", "West", "South"])
    update_current_location(y_coordinate, x_coordinate, direction)


def find_current_location():
    print("Current location")
    with open("character.json", "r") as file_object:
        character_dictionary = json.load(file_object)
        x_coordinate = character_dictionary["X-coordinate"]
        y_coordinate = character_dictionary["Y-coordinate"]
        describe_current_location(y_coordinate, x_coordinate)


def run():
    find_current_location()


def main():
    run()


if __name__ == "__main__":
    main()
