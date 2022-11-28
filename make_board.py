def make_board():
    white_house_map = [[[0, 1, 1, 1],
                       [0, 1, 1, 1]],

                       [[0, 0, 1],
                       [0, 0, 1, 0, 0, 1, 1, 0],
                       [0, 0, 1, 0, 0, 1, 0, 0],
                       [0, 0, 1, 0, 0, 1, 0, 0],
                       [0, 1, 1, 1, 1, 1, 0, 0]],

                       [[0, 0, 1, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 0, 1, 1, 1],
                       [0, 0, 1, 0, 0, 1, 1, 1],
                       [0, 1, 1, 1, 1, 1, 1, 1],
                       [0, 0, 1, 0, 0, 0, 0, 0]],

                       [[0, 0, 1, 0, 0, 0, 0, 0],
                       [0, 1, 1, 1, 0, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1],
                       [0, 1, 1, 1, 0, 1, 1, 1],
                       [0, 0, 1, 0]]]
    for level in white_house_map:
        print("This is another level")
        print()
        for row in level:
            print("\t", end="")
            for room in row:
                if room == 1:
                    print("[]", end="")
                else:
                    print("  ", end="")
            print()


def main():
    make_board(10, 10)


if __name__ == "__main__":
    main()
