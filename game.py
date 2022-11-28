"""
Ankit Ahlwat / A01317232 / ankitahlwat

Jas Randhawa / A01236951 / jasbcit
"""


def game():
    rows = 10
    columns = 10
    board = make_board(rows, columns)
    character = make_character("Player Name")
    achieved_goal = False
    while not achieved_goal:
        describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character)
            describe_current_location(board, character)
            there_is_a_challenge = check_for_challenges()
            if there_is_a_challenge:
                execute_challenge_protocol(character)
                if character_has_leveled():
                    execute_glow_up_protocol()
                achieved_goal = check_if_goal_attained(board, character)
        else:
            pass


def main():
    game()


if __name__ == '__main__':
    main()
