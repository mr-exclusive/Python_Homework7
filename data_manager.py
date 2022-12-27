import io_manager

data_format = 0
contacts = []
field_names = ('Last name: ', 'Name: ', 'Middle name: ', 'Phone: ', 'Comment: ')


def init_phonebook(display_format):
    global contacts
    global data_format
    data_format = display_format
    contacts = io_manager.read_contacts(data_format)


def add_contact():
    last_name = input('Enter last name: ')
    first_name = input('Enter first name: ')
    middle_name = input('Enter middle name: ')
    phone = input('Enter phone number: ')
    comment = input('Enter comment: ')

    contact = [last_name, first_name, middle_name, phone, comment]
    contacts.append(contact)
    print('--> Contact is added to the phonebook!')


def print_contacts():
    if len(contacts) == 0:
        print('(empty)')
    else:
        for i, contact in enumerate(contacts, start=1):
            print_contact(i, contact)


def print_contact(ind, contact):
    if data_format == 1:  # in one line
        print(f'{ind}. {", ".join(contact)}')
    else:  # every field on new line
        print(f'### {ind} ###')
        for i, field in enumerate(contact):
            print(f'{field_names[i]}{field if field else "(empty)"}')


def search_contacts():
    return


def delete_contact():
    flag = True
    while flag:
        try:
            delete_id = int(input("Enter contact's id to delete (or 0 to exit): "))
            if 1 <= delete_id <= len(contacts):
                del contacts[delete_id-1]
                print(f"--> Contact with 'id'={delete_id} successfully deleted!")
                flag = False
            elif delete_id == 0:
                flag = False
            else:
                print(f"--> Contact is NOT found for specified 'id'={delete_id}.")
        except ValueError:
            print("--> 'id' must be a number!")


def edit_contact():
    return


def save_contacts():
    io_manager.save_contacts(contacts, data_format)
