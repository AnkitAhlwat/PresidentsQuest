import json


def make_board():
    icons = {
        "0": "   ",
        "1": "[ ]",
        "S": "[S]",
        "B": "[B]",
        "C": "[X]"
    }
    with open("white_house.txt", 'r') as white_house_map:
        coordinates = {}
        board = white_house_map.readlines()
        for index_row, row in enumerate(board):
            for index_room, room in enumerate(row):
                if room != "\n":
                    coordinates[f'{index_row}:{index_room}'] = icons.get(room)
        with open("coordinates.json", "w") as file_object:
            json.dump(coordinates, file_object)


def main():
    make_board()


if __name__ == "__main__":
    main()
