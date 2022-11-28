def make_board():
    map_icons ={
        "0": "\U00002B1B",
        "1": "\U00002B1C",
        "S": "\U0001F6D2",
        "B": "\U00002694",
        "C": "\U0001F935"

    }
    with open("white_house.txt", 'r') as white_house_map:
        board = white_house_map.readlines()
        for row in board:
            print("\t", end="")
            for room in row:
                if room in map_icons:
                    print(f'{map_icons[room]}', end="")
            print()


def main():
    make_board()


if __name__ == "__main__":
    main()
