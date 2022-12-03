import json

from get_user_choice import get_user_choice


def format_weapons_list(list_item):
    mapped_list = []

    for item in list_item:
        child_list = item[0] + " | " + "Cost: " + str(item[1]) + " | " + "Attack Gained: " + str(item[2])
        mapped_list.append(child_list)

    return mapped_list


def format_food_list(list_item):
    mapped_list = []

    for item in list_item:
        child_list = item[0] + " | " + "Cost: " + str(item[1]) + " | " + "Health Gained: " + str(item[2])
        mapped_list.append(child_list)

    return mapped_list

def update_player(player):
    with open("character.json", "w") as file_object:
        json.dump(player,file_object)
def add_to_inventory(item, player):
    player["Items"].append(item)
    return


def adjust_player_attack(item, player):
    player['Attack Points'] += item
    return


def adjust_player_health(item, player):
    if item >= player['Max HP']:
        player['Current HP'] = player['Max HP']
    else:
        player['Current HP'] += item
    if player['Current HP'] > player['Max HP']:
        player['Current HP'] = player['Max HP']
    return


def buy_item(item_type, selected_item, player):
    if int(player["Money"]) >= int(selected_item[1].replace("Cost: ", "")):
        player["Money"] = int(player["Money"]) - int(selected_item[1].replace("Cost: ", ""))
        if item_type == 'weapon':
            add_to_inventory(selected_item[0], player)
            adjust_player_attack(int(selected_item[2].replace("Attack Gained: ", "")), player)
        else:
            adjust_player_health(int(selected_item[2].replace("Health Gained: ", "")), player)
        return True
    else:
        return False


def shopkeeper(player):
    weapons_dictionary = {
        1:
            ["The President's Coffee Mug", 1, 1],
        2:
            ["Republican Hat", 1, 1],
        3:
            ["Democrat Hat", 1, 1],
        4:
            ["Bible", 5, 5],
        5:
            ["Unfinished Memo to Justin Trudeau", 6, 8],
        6:
            ["Presidential Pen", 10, 12],
        7:
            ["Painting of Abraham Lincoln", 12, 15],
        8:
            ["Seized Documents from Mar-a-Lago", 15, 22],
        9:
            ["Bald Eagle", 20, 50],
        10:
            ["The Constitution", 40, 80]
    }

    food_dictionary = {
        1:
            ["Bourbon", 1, 2],
        2:
            ["Turkey", 2, 4],
        3:
            ["Chicago-style Pizza", 3, 6],
        4:
            ["Cheeseburger", 4, 7],
        5:
            ["Philly Cheese Steak", 5, 10],
        6:
            ["Nashville Hot Chicken", 8, 20],
        7:
            ["Melania's Homemade Dinner from 2019", 15, 35],
        8:
            ["Barack's Sandwich from 2015", 25, 100]
    }

    if player["Visited Shop"]:
        print(f"Great to see you again, {player['Name']}!\n")
        print(f"You currently have {player['Current HP']} HP and {player['Attack Points']} Attack Points.\n")
    else:
        print(f"Welcome to the White House Gift Shop, {player['Name']}.\n")
        print("Here you can purchase weapons to level up your attack points or purchase food to heal your health"
              "points.\n")
        print(f"Your Stats:\n{player['Current HP']}/{player['Max HP']} HP     {player['Attack Points']} "
              f"Attack Points    ${player['Money']}\n")

    in_the_shop = True

    while in_the_shop:
        user_selection = get_user_choice('shopchoice', "What would you like to do?", ['Buy Weapons', 'Buy Food',
                                                                                      'Leave'])
        if user_selection == 'Leave':
            in_the_shop = False
            player['Visited Shop'] = True
            print("\nThank you for visiting the shop!\n")
            print(
                f"You now have {player['Current HP']}/{player['Max HP']} HP and {player['Attack Points']} "
                f"Attack Points.")
            print(f"Remaining Balance: ${player['Money']}.\n")
            print("Hope to see you soon...")
            update_player(player)


        elif user_selection == 'Buy Weapons':
            mapped_weapons_list = map(format_weapons_list, [weapons_dictionary.values()])
            weapon_selected = get_user_choice('weapons-choice', 'What weapon would you like to buy?',
                                              [child for item in mapped_weapons_list for child in item])

            selected_item_as_list = weapon_selected.split(" | ")
            can_user_buy_item = buy_item('weapon', selected_item_as_list, player)

            if can_user_buy_item:
                print(f"You bought {selected_item_as_list[0]}. A fine choice! \n")
                print(f"You now have {player['Attack Points']} Attack Points.")
                print(f"Remaining Balance: ${player['Money']}.\n")

            else:
                print(f"Sorry, you do not have enough money to purchase the {selected_item_as_list[0]}.")
                print(f"Current Balance: ${player['Money']}.\n")

        elif user_selection == 'Buy Food':
            mapped_food_list = map(format_food_list, [food_dictionary.values()])
            food_selected = get_user_choice('food-choice', 'What food would you like to buy?',
                                            [child for item in mapped_food_list for child in
                                             item])

            selected_item_as_list = food_selected.split(" | ")
            can_user_buy_item = buy_item('food', selected_item_as_list, player)

            if can_user_buy_item:
                print(f"You bought {selected_item_as_list[0]}. A fine choice! \n")
                print(f"You now have {player['Current HP']}/{player['Max HP']} HP.")
                print(f"Remaining Balance: ${player['Money']}.\n")

            else:
                print(f"Sorry, you do not have enough money to purchase the {selected_item_as_list[0]}.")
                print(f"Current Balance: ${player['Money']}.")

def setup_shopkeeper():
    with open("character.json", "r+") as file_object:
        player = json.load(file_object)
        shopkeeper(player)

def main(player=None):
    # player = {'Name': 'Jas', 'Visited Shop': False, 'Money': 10, 'Items': [], 'Attack Points': 0, 'Current HP': 0,
    #           'Max HP': 5}
    setup_shopkeeper()


if __name__ == '__main__':
    main()
