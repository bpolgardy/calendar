import ui
# import storage


def initialize_calendar():
    calendar = {}
    return calendar


def schedule_meeting_in(calendar):
    meeting_title = ui.get_user_input('Enter meeting title', str)
    duration = ui.get_user_input('Enter duration in hours (1 or 2)', int, 'duration')
    start_time = ui.get_user_input('Enter start time', int, 'start_time')

    print(duration, start_time, meeting_title)

    # calendar[start_time] = meeting_title


def main():
    calendar = initialize_calendar()

    while True:
        ui.print_menu()
        user_choice = ui.get_user_input('Enter choice', str)
        if user_choice == 's':
            schedule_meeting_in(calendar)
        elif user_choice == 'c':
            pass
        elif user_choice == 'q':
            break
        else:
            ui.print_message('No such option!')


if __name__ == '__main__':
    main()
