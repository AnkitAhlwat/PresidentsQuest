from get_user_choice import get_user_choice


def shopkeeper(player):
    weapons_dictionary = {
        "The President's Coffee Mug": {
            'User Level Required': 1,
            'Weapon Cost': 1,
            'Attack Gain': 1
        },
        'Republican Hat': {
            'User Level Required': 1,
            'Weapon Cost': 1,
            'Attack Gain': 1
        },
        'Democrat Hat': {
            'User Level Required': 1,
            'Weapon Cost': 1,
            'Attack Gain': 1
        },
        'Bible': {
            'User Level Required': 1,
            'Weapon Cost': 5,
            'Attack Gain': 5
        },
        'Unfinished Memo to Justin Trudeau': {
            'User Level Required': 2,
            'Weapon Cost': 6,
            'Attack Gain': 8
        },
        'Presidential Pen': {
            'User Level Required': 2,
            'Weapon Cost': 10,
            'Attack Gain': 12
        },
        'Painting of Abraham Lincoln': {
            'User Level Required': 2,
            'Weapon Cost': 12,
            'Attack Gain': 15
        },
        'Seized Documents from Mar-a-Lago': {
            'User Level Required': 2,
            'Weapon Cost': 15,
            'Attack Gain': 22
        },
        'Bald Eagle': {
            'User Level Required': 3,
            'Weapon Cost': 20,
            'Attack Gain': 50
        },
        'The Constitution': {
            'User Level Required': 3,
            'Weapon Cost': 40,
            'Attack Gain': 80
        },
    }
    food_dictionary = {
        "Bourbon": {
            'Food Cost': 1,
            'Health Recovered': 2
        },
        "Turkey": {
            'Food Cost': 2,
            'Health Recovered': 4
        },
        "Chicago-style Pizza": {
            'Food Cost': 3,
            'Health Recovered': 6
        },
        "Cheeseburger": {
            'Food Cost': 4,
            'Health Recovered': 7
        },
        "Philly Cheese Steak": {
            'Food Cost': 5,
            'Health Recovered': 10
        },
        "Nashville Hot Chicken": {
            'Food Cost': 8,
            'Health Recovered': 20
        },
        "Melania's Homemade Dinner from 2019": {
            'Food Cost': 15,
            'Health Recovered': 35
        },
        "Barack's Sandwich from 2015 ": {
            'Food Cost': 25,
            'Health Recovered': 100
        },
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
        weapons_bought = get_user_choice('weapons-choice', 'What weapons would you like to buy?',
                                         weapons_dictionary.keys())
    elif initial_selection == 'Buy Food':
        food_bought = get_user_choice('food-choice', 'What food would you like to buy?', food_dictionary.keys())


def main():
    player = {'Name': 'Jas', 'Visited Shop': True, 'Gold': 0}
    shopkeeper(player)


if __name__ == '__main__':
    main()
