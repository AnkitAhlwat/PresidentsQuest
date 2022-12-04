import json

import run_game
from die import Die
from time import sleep
import combat
def open_loot(y_coordinate,x_coordinate):
    with open("character.json", "r") as file_object:
        player = json.load(file_object)
    loot_die = Die(10)
    xp_result = loot_die.roll_die()
    gold_result = loot_die.roll_die()
    print("Oh looks like I found a chest...")
    sleep(2)
    print(f'Congratulations, you received {xp_result} XP and {gold_result} gold!')
    player["XP"] +=xp_result
    player["Money"] += gold_result
    combat.check_if_level_up(player)
    with open("character.json", "w") as file_object:
        json.dump(player, file_object)
    with open("coordinates.json", "r") as file_object:
        coordinates_map = json.load(file_object)
    coordinates_map[f'{y_coordinate}:{x_coordinate}'] = "[ ]"
    with open("coordinates.json", "w") as file_object:
        json.dump(coordinates_map, file_object)
    run_game.setup_current_location()
def main():
    open_loot(y_coordinate=None, x_coordinate=None)


if __name__ == '__main__':
    main()
