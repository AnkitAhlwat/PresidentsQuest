from get_user_choice import get_user_choice


def shopkeeper(player):
    weapons_dictionary = {
        "The President's Coffee Mug": (1, 1, 1),
        'Republican Hat': (1, 1, 1),
        'Democrat Hat': (1, 1, 1),
        'Bible': (1, 5, 5),
        'Unfinished Memo to Justin Trudeau': (2, 6, 8),
        'Presidential Pen': (2, 10, 12),
        'Painting of Abraham Lincoln': (2, 12, 15),
        'Seized Documents from Mar-a-Lago': (2, 15, 22),
        'Bald Eagle': (3, 20, 50),
        'The Constitution': (3, 40, 80)
    }
    food_dictionary = {
        "Bourbon": (1, 2),
        "Turkey": (2, 4),
        "Chicago-style Pizza": (3, 6),
        "Cheeseburger": (4, 7),
        "Philly Cheese Steak": (5, 10),
        "Nashville Hot Chicken": (8, 20),
        "Melania's Homemade Dinner from 2019": (15, 35),
        "Michelle's Totally-Not-Gone-Bad Breakfast from 2016": (25, 100)
    }

    if player["Visited Shop"]:
        print(f"Great to see you again, {player['Name']}!\n")
    else:
        print(f"Welcome to the White House Gift Shop, {player['Name']}.\n")
        print("Here you can purchase weapons to level up your attack points or purchase food to heal your health"
              "points.\n")

    initial_selection = get_user_choice('shopchoice', "What would you like to do?", ['Buy Weapons', 'Buy Food',
                                                                                     'Leave'])

    if initial_selection == 'Leave':
        print("See ya later alligator!")
    elif initial_selection == 'Buy Weapons':
        get_user_choice('weapons-choice', 'What weapons would you like to buy?', weapons_dictionary.keys())


def main():
    player = {'Name': 'Jas', 'Visited Shop': True, 'Gold': 0}
    shopkeeper(player)


if __name__ == '__main__':
    main()
