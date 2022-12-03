import json
import combat
import chest
import shopkeeper
from get_user_choice import get_user_choice
from die import Die
from colorama import Fore, Style
from time import sleep


def run_totally_cool_celebration_protocol():
    print("What did you expect a cool celebration or something? Scram kid your the president now go do some work")
    quit()


def check_if_goal_achieved():
    with open("character.json", "r") as file_object:
        character_dictionary = json.load(file_object)
        if character_dictionary["Achieved Goal"]:
            run_totally_cool_celebration_protocol()


def display_map():
    with open("coordinates.json") as file_object:
        coordinates = json.load(file_object)
    print(Fore.MAGENTA + "Current map" + Style.RESET_ALL + "\n")

    position = 0
    for room, icons in coordinates.items():
        print(icons, end="")
        position += 1
        if position == 8:
            print()
            position = 0


def check_for_event(coordinates):
    with open("event.json", "r") as file_object:
        event = json.load(file_object)
        event_function = event[coordinates]
        eval(f'{event_function}()')



def check_for_random_enemy():
    current_die = Die(10)
    dice_roll = current_die.roll_die()
    if dice_roll <= 1:
        print("A wild enemy politician appeared!")
        combat.setup_combat()
        find_current_location()


def is_valid_move(current_location):
    with open("coordinates.json", "r") as file_object:
        coordinates = json.load(file_object)
        if current_location not in coordinates or coordinates[current_location] == "   ":
            return False
        return True


def update_current_location(y_coordinate, x_coordinate, direction):
    y_map = {"North": -1, "South": +1, "West": 0, "East": 0, None: 0}
    x_map = {"West": -1, "East": +1, "North": 0, "South": 0, None: 0}

    with open("coordinates.json", "r") as file_object:
        coordinates = json.load(file_object)

    with open("character.json", "r") as file_object:
        character_dictionary = json.load(file_object)

    if is_valid_move(f'{y_coordinate + y_map[direction]}:{x_coordinate + x_map[direction]}'):
        y_coordinate += y_map[direction]
        x_coordinate += x_map[direction]

        coordinates[f'{character_dictionary["Y-coordinate"]}:{character_dictionary["X-coordinate"]}'] = "[ ]"
        character_dictionary["Y-coordinate"] = y_coordinate
        character_dictionary["X-coordinate"] = x_coordinate
        check_for_event(coordinates[f'{y_coordinate}:{x_coordinate}'])
        coordinates[f'{character_dictionary["Y-coordinate"]}:{character_dictionary["X-coordinate"]}'] = \
            Fore.BLUE + "[X]" + Style.RESET_ALL

        with open("character.json", "w") as file_object:
            json.dump(character_dictionary, file_object)
        with open("coordinates.json", "w") as file_object:
            json.dump(coordinates, file_object)
        describe_current_location(y_coordinate, x_coordinate)

    else:
        print(Fore.RED + "That is not a valid move try again" + Style.RESET_ALL + "\n")
        sleep(1.5)
        describe_current_location(y_coordinate, x_coordinate)


def describe_current_location(y_coordinate, x_coordinate):
    display_map()
    with open("white_house_room_descriptions.json", "r") as file_object:
        room_description_dictionary = json.load(file_object)
        print("\n" + room_description_dictionary[f'{y_coordinate}:{x_coordinate}'])
    direction = get_user_choice("Decision", "Where would you like to go", ["North", "East", "West", "South",
                                                                           "Quit Game"])
    if direction == "Quit Game":
        confirmation = get_user_choice("Confirmation", "Are you sure?", ["No I want to play", "Yes"])
        if confirmation == "Yes":
            return quit()
        else:
            setup_current_location()
    update_current_location(y_coordinate, x_coordinate, direction)


def find_current_location():
    with open("character.json", "r") as file_object:
        character_dictionary = json.load(file_object)
        if character_dictionary["Achieved Goal"]:
            quit()
        x_coordinate = character_dictionary["X-coordinate"]
        y_coordinate = character_dictionary["Y-coordinate"]
        update_current_location(y_coordinate, x_coordinate, direction=None)


def setup_current_location():
    find_current_location()


def setup_game():
    setup_current_location()


def main():
    setup_current_location()


if __name__ == "__main__":
    main()
