from get_user_choice import get_user_choice
from time import sleep
from enemy import Enemy
import json
import random
import describe_current_location
from colorama import Fore, Style


def combat_opening_interaction(enemy, player):
    with open('interactions.json') as file:
        interactions = json.load(file)

    republican_openers = [opener for value in interactions['battleOpeners'][0].values() for opener in value]
    democrat_openers = [opener for value in interactions['battleOpeners'][1].values() for opener in value]

    if player['Political Party'] == "Democrat":
        return enemy.name + ": " + republican_openers[random.randint(0, len(republican_openers) - 1)]
    elif player['Political Party'] == "Republican":
        return enemy.name + ": " + democrat_openers[random.randint(0, len(democrat_openers) - 1)]
    else:
        return "Prepare to die!"


def fight_or_leave():
    return get_user_choice('fight-or-leave', 'What would you like to do?',
                           ["Fight", "Leave"])


def roll_die(sides):
    return random.randint(1, sides - 1)


def check_health(player_hp, enemy_hp):
    if player_hp <= 0:
        print(Fore.RED + "You died")
        return True
    elif enemy_hp <= 0:
        print(Fore.GREEN + "You defeated the enemy!")
        return True
    else:
        return False


def check_player_inventory(enemy, player):
    if enemy.name == "Donald Trump" or enemy.name == "Joe Biden":
        if player["Items"].count("The Constitution") >= 1:
            return True
        else:
            print(enemy.name + ": You don't have The Constitution on you... You're not worth my time!")
            return False
    elif enemy.name == "George W. Bush" or enemy.name == "Bernie Sanders":
        if player["Items"].count("Bald Eagle") >= 1:
            return True
        else:
            print(enemy.name + ": You don't have a Bald Eagle on you... I pity your very existence!")
            return False
    elif enemy.name == "Ted Cruz" or enemy.name == "Alexandria Ocasio-Cortez":
        if player["Items"].count("Presidential Pen") >= 1:
            return True
        else:
            print(enemy.name + ": You don't have the Presidential Pen on you... Get out of my sight!")
            return False
    else:
        return True


def fight(enemy, player, difficulty):
    player_hp = player["Current HP"]
    player_attack = player["Attack Points"]
    enemy_hp = enemy.hp
    enemy_attack = enemy.attack

    if difficulty == "Easy":
        player_roll_needed = 2
        enemy_roll_needed = 8
    elif difficulty == "Medium":
        player_roll_needed = 4
        enemy_roll_needed = 4
    else:
        player_roll_needed = 8
        enemy_roll_needed = 2

    in_combat = True
    while in_combat:

        player_roll = roll_die(10)
        sleep(2)
        if player_roll >= player_roll_needed:
            enemy_hp -= player_attack
            print(Fore.GREEN + "Your hit landed!")
            if enemy_hp < 0:
                print("The enemy has 0HP left.")
            else:
                print("The enemy has " + str(enemy_hp) + "HP left.")
            print()
        else:
            enemy_hp += 0
            print("Your hit missed!")
            print()
        sleep(2)

        is_dead = check_health(player_hp, enemy_hp)
        if is_dead:
            print(Style.RESET_ALL)
            break

        enemy_roll = roll_die(10)
        if enemy_roll >= enemy_roll_needed:
            player_hp -= enemy_attack
            print(Fore.RED + "The enemy's hit landed!")
            if player_hp < 0:
                print("You now have 0HP left.")
            else:
                print("You now have " + str(player_hp) + "HP left.")
            print()
        else:
            player_hp += 0
            print(Fore.RED + "The enemy's hit missed!")
            print()
        sleep(2)

        is_dead = check_health(player_hp, enemy_hp)
        if is_dead:
            print(Style.RESET_ALL)
            break
    return

def combat(enemy, player, difficulty):
    print(combat_opening_interaction(enemy, player))
    print()
    user_choice = fight_or_leave()
    if user_choice == "Fight":
        is_fight_valid = check_player_inventory(enemy, player)
        if is_fight_valid:
            fight(enemy, player, difficulty)
        describe_current_location.setup_current_location()
    else:
        describe_current_location.setup_current_location()


def setup_boss():
    with open("character.json", "r") as file_object:
        player = json.load(file_object)

    with open("character.json", "r") as file_object:
        character_dictionary = json.load(file_object)
        party = character_dictionary["Political Party"]

    democrat_boss = ["Alexandria Ocasio-Cortez", "Bernie Sanders", "Joe Biden"]
    republican_boss = ["Ted Cruz", "George W. Bush", "Donald Trump"]
    if party == "Republican":
        level_one_boss = Enemy(democrat_boss[0], "Boss", 1, 10, 4)
        level_two_boss = Enemy(democrat_boss[1], "Boss", 1, 10, 4)
        level_three_boss = Enemy(democrat_boss[2], "Boss", 1, 10, 4)
    else:
        level_one_boss = Enemy(republican_boss[0], "Boss", 1, 10, 4)
        level_two_boss = Enemy(republican_boss[1], "Boss", 1, 10, 4)
        level_three_boss = Enemy(republican_boss[2], "Boss", 1, 10, 4)

    combat(level_one_boss, player, "Medium")
def setup_combat():
    mike_pence = Enemy("Mike Pence", "Minion", 1, 5, 2)
    with open("character.json", "r") as file_object:
        player = json.load(file_object)
    # player['Items'] = "The Constitution"
    combat(mike_pence, player, "Easy")


def main():
    setup_boss()
    mike_pence = Enemy("Mike Pence", "Minion", 1, 5, 2)
    # player = character('John', 'Republican')
    # player['Items'] = "The Constitution"
    # combat(mike_pence, player, "Easy")


if __name__ == '__main__':
    main()
