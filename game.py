"""
Ankit Ahlwat / A01317232 / ankitahlwat

Jas Randhawa / A01236951 / jasbcit
"""
from make_board import make_board
from make_character import make_character
from describe_current_location import *
def game():
    make_board()
    make_character("Player Name", "Republican")
    achieved_goal = False
    while not achieved_goal:
        setup_current_location()
        # if character_has_leveled():
        #     execute_glow_up_protocol()
        # achieved_goal = check_if_goal_attained(board, character)

def main():
    game()


if __name__ == '__main__':
    main()
