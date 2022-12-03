"""
Ankit Ahlwat / A01317232 / ankitahlwat

Jas Randhawa / A01236951 / jasbcit
"""
from make_board import make_board
from make_character import make_character
from describe_current_location import *


def game():
    achieved_goal = False
    while not achieved_goal:
        setup_current_location()
        # if character_has_leveled():
        #     execute_glow_up_protocol()
        # achieved_goal = check_if_goal_attained(board, character)


def main():
    try:
        with open("characters.json", "r"):
            print("Welcome back")
    except FileNotFoundError:
        make_board()
        player_name = input("Please enter your name: ")
        party = get_user_choice("Party","Please select your party", ["Democrat", "Republican"])
        make_character(player_name, party)
    game()


if __name__ == '__main__':
    main()
