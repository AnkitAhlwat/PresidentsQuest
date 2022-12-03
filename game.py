"""
Ankit Ahlwat / A01317232 / ankitahlwat

Jas Randhawa / A01236951 / jasbcit
"""
import run_game
from make_board import make_board
from make_character import make_character
from run_game import *


def game():
    run_game.setup_game()


def main():
    try:
        with open("character.json", "r"):
            print("Welcome back")
    except FileNotFoundError:
        make_board()
        player_name = input("Please enter your name: ")
        party = get_user_choice("Party", "Please select your party", ["Democrat", "Republican"])
        make_character(player_name, party)
    game()


if __name__ == '__main__':
    main()
