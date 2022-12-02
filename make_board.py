import json
def make_board():
    visual_icons = {
        "0": "\U00002B1B",
        "1": "\U00002B1C",
        "S": "\U0001F6D2",
        "B": "\U00002694",
        "C": "\U0001F935"

    }
    cmd_icons = {
        "0": "   ",
        "1": "[ ]",
        "S": "[S]",
        "B": "[B]",
        "C": "[X]"
    }
    with open("white_house.txt", 'r') as white_house_map:
        coordinates = {}
        board = white_house_map.readlines()
        with open("character.json", "r") as file_object:
            character_dictionary = json.load(file_object)
            icons = character_dictionary['Icons']
            if icons == "cmd":
                map_icons = cmd_icons
            else:
                map_icons = visual_icons
        for index_row, row in enumerate(board):
            for index_room, room in enumerate(row):
                if room != "\n":
                    coordinates[f'{index_row}:{index_room}'] = map_icons.get(room)
        with open("coordinates.json", "w") as file_object:
            json.dump(coordinates, file_object)

def main():
    make_board()


if __name__ == "__main__":
    main()
