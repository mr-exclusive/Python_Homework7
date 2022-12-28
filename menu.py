import data_manager as dm


def print_format_menu():
    print('Select display format for the "Phone Book":')
    print('[1] In one line')
    print('[2] Every field on separate line')
    print('[0] Exit\n')


def print_menu():
    print('**********MENU**********')
    print('[1] Show all contacts')
    print('[2] Search contacts (not implemented)')
    print('[3] Add contact')
    print('[4] Delete contact')
    print('[5] Edit contact (not implemented)')
    print('[0] Exit')
    print('************************')


def print_error():
    print('--> Invalid input!')


def start_program():
    invite_text = 'Select a menu number from any of the above: '
    show_format_menu = True
    while show_format_menu:
        print_format_menu()

        try:
            command = int(input(invite_text))

            if command == 1 or command == 2:
                dm.init_phonebook(command)  # set format and read contacts from a file

                show_menu = True
                while show_menu:
                    print_menu()

                    try:
                        command = int(input(invite_text))

                        if command == 1:  # [1] Show all contacts
                            dm.print_contacts()
                        elif command == 2:  # [2] Search contacts (not implemented)
                            dm.search_contacts()
                        elif command == 3:  # [3] Add contact
                            dm.add_contact()
                        elif command == 4:  # [4] Delete contact
                            dm.delete_contact()
                        elif command == 5:  # [5] Edit contact (not implemented)
                            dm.edit_contact()
                        elif command == 0:  # [0] Exit -> format selection
                            dm.save_contacts()
                            show_menu = False
                        else:
                            print_error()
                    except ValueError:
                        print_error()

            elif command == 0:  # [0] Exit -> program
                show_format_menu = False
            else:
                print_error()
        except ValueError:
            print_error()
