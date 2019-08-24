def get_user_input(prompt, required_type):
    valid_input_entered = False

    while not valid_input_entered:
        try:
            user_input = input(f'{prompt}: ')

            if required_type == str and user_input.isalpha():
                break

            elif required_type == int and user_input.isnumeric():
                break

            else:
                raise ValueError(f'Please enter a valid {prompt[6:]}!')

        except ValueError as err:
            print(err)

    return user_input


def print_menu():
    print('\033c', end='')
    print('Menu:')
    print('(s) schedule a new meeting')
    print('(c) cancel an existing meeting')
    print('(q) quit')


def print_message(message):
    print(message)
    input('Press ENTER to continue...')
