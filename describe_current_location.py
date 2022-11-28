import json
from get_user_choice import get_user_choice


def display_map(coordinates):
    print("Current map")
    position = 0
    for room, icons in coordinates.items():
        print(icons, end="")
        position += 1
        if position == 8:
            print()
            position = 0


def describe_current_location(current_location):
    with open("white_house_room_descriptions.json", "r") as file_object:
        room_description_dictionary = json.load(file_object)
        print(room_description_dictionary[current_location])
    get_user_choice("Decison","What would you like to do", ["Fight","Run","Examine"])


def find_current_location(coordinates):
    print("Current location")
    for coordinate, room in coordinates.items():
        if room == "🤵":
            current_location = coordinate
            describe_current_location(current_location)

def run():
    with open("coordinates.json") as file_object:
        coordinates = json.load(file_object)
    display_map(coordinates)
    find_current_location(coordinates)


def main():
    run()


if __name__ == "__main__":
    main()
