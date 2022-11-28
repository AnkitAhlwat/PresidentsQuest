import json


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

def find_current_location(coordinates):
    print("Current location")
    for coordinate, room in coordinates.items():
        if room == "🤵":
            current_location = coordinate
            describe_current_location(current_location)

def main():
    with open("coordinates.json") as file_object:
        coordinates = json.load(file_object)
    display_map(coordinates)
    find_current_location(coordinates)



if __name__ == "__main__":
    main()
