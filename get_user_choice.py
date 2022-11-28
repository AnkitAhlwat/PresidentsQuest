from pick import pick


def get_user_choice():

    title = 'Please choose your favorite programming language: '
    options = ['Java', 'JavaScript', 'Python', 'PHP', 'C++', 'Erlang', 'Haskell']
    enumerate_options = enumerate(options)
    option, index = pick(list(enumerate_options), title)

    print(option)
    print(index)


def main():
    get_user_choice()


if __name__ == "__main__":
    main()
