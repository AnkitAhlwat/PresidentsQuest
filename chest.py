import json

from die import Die
from time import sleep
from combat import check_if_level_up
def open_loot():
    with open("character.json", "r") as file_object:
        player = json.load(file_object)
    loot_die = Die(10)
    xp_result = loot_die.roll_die()
    gold_result = loot_die.roll_die()
    print("Oh looks like I found a chest...")
    sleep(2)
    print(f'Congratulations, you received {xp_result} XP and {gold_result} gold!')
    check_if_level_up(player)

def main():
    open_loot()


if __name__ == '__main__':
    main()
