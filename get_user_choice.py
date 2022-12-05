import inquirer
import os
import platform


def get_user_choice(questiontype, prompt, choices):

    questions = [
        inquirer.List(questiontype,
                      message=prompt,
                      choices=choices
                      ),
    ]

    answers = inquirer.prompt(questions)
    if platform.system() == "Darwin":
        os.system("clear")
    else:
        os.system('cls')
    return answers[questiontype]


def main(questiontype=None, prompt=None, choices=None):
    get_user_choice(questiontype, prompt, choices)


if __name__ == "__main__":
    main()
