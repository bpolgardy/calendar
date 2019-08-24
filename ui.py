def get_user_input(prompt, required_type, entry_type=None):
    valid_input_entered = False
    while not valid_input_entered:
        try:
            user_input = input(f'{prompt}: ')

            if required_type == str and user_input.isalpha():
                break

            elif required_type == int and user_input.isnumeric():
                valid_input_entered = validate_permitted_values_in(user_input, entry_type)

            else:
                raise ValueError(f'Please enter a valid {prompt[6:]}!')

        except ValueError as err:
            print(err)

    return user_input


def validate_permitted_values_in(user_input, entry_type):
    if entry_type == 'duration':
        PERMITTED_VALUES = 1, 2
        if int(user_input) in PERMITTED_VALUES:
            return True
        else:
            raise ValueError('Meeting duration can only be 1 hour or 2 hours!')

    elif entry_type == 'start_time':
        if 8 <= int(user_input) <= 18:
            return True
        elif int(user_input) < 0 or int(user_input) > 23:
            raise ValueError('Invalid time provided!')
        else:
            raise ValueError('Meeting is outside your working hours!')

    return False


def print_menu():
    print('\033c', end='')
    print('Menu:')
    print('(s) schedule a new meeting')
    print('(c) cancel an existing meeting')
    print('(q) quit')


def print_message(message):
    print(message)
    input('Press ENTER to continue...')
