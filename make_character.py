def make_character(name, party):
    character_dictionary = {
        'Name': name,
        'X-coordinate': 0,
        'Y-coordinate': 0,
        'Level': 0,
        'Current HP': 5,
        'Max HP': 5,
        'Money': 0,
        'Attack Points': 1,
        'Visited Shop': False,
        'Items': [],
        'Political Party': party
    }
    return character_dictionary


def main():
    make_character(input("Name? "))


if __name__ == "__main__":
    main()
