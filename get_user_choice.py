import inquirer
import os

def get_user_choice(questiontype, prompt, choices):
    # title = prompt
    # options = choices
    # enumerate_options = enumerate(options)
    # option, index = pick(list(enumerate_options), title)
    questions = [
        inquirer.List(questiontype,
                      message=prompt,
                      choices=choices
                      ),
    ]

    answers = inquirer.prompt(questions)
    os.system('cls')
    return answers[questiontype]


def main(questiontype=None, prompt=None, choices=None):
    get_user_choice(questiontype, prompt, choices)


if __name__ == "__main__":
    main()
