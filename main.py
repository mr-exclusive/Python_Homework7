import menu
import data_manager as dm


if __name__ == '__main__':
    invite_text = 'Select a menu number from any of the above: '
    show_format_menu = True
    while show_format_menu:
        menu.print_format_menu()

        try:
            command = int(input(invite_text))

            if command == 1 or command == 2:
                dm.init_phonebook(command)  # set format and read contacts from a file

                show_menu = True
                while show_menu:
                    menu.print_menu()

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
                            menu.print_error()
                    except ValueError:
                        menu.print_error()

            elif command == 0:  # [0] Exit -> program
                show_format_menu = False
            else:
                menu.print_error()
        except ValueError:
            menu.print_error()
