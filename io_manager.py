import os


def get_params(data_format):
    if data_format == 1:  # in one line
        return 'phonebook1.txt', ', ', '\n'
    else:  # every field on new line
        return 'phonebook2.txt', '\n', '\n***\n'


def read_contacts(data_format):
    file_name, sep1, sep2 = get_params(data_format)

    if os.path.isfile(file_name):
        if os.stat(file_name).st_size != 0:
            with open(file_name, "r", encoding="utf_8") as f:
                return list(map(lambda x: x.split(sep1), f.read().split(sep2)))

    return list()


def save_contacts(contacts, data_format):
    file_name, sep1, sep2 = get_params(data_format)

    with open(file_name, "w", encoding="utf_8") as f:
        f.write(sep2.join([sep1.join(contact) for contact in contacts]))
