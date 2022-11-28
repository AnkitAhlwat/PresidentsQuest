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


def describe_current_location(coordinates):
    print("Current position")
    for coordinate, room in coordinates.items():
        if room == "🤵":
            print(coordinate, room)


def main():
    with open("coordinates.json") as file_object:
        coordinates = json.load(file_object)
    display_map(coordinates)
    describe_current_location(coordinates)



if __name__ == "__main__":
    main()
