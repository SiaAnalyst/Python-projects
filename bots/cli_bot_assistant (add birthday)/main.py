from classes import AddressBook, Record, Name, Phone, Birthday
from re import search

# create address book
ADDRESS_BOOK = AddressBook()

# decorator to handle user input errors
def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except ValueError as value_error:
            return value_error
        except KeyError as key_error:
            return key_error
        except IndexError:
            return 'Please type: name and phone number'
        except TypeError:
            return "No command found. Please type one of this: hello, add [Name] [phone], change [Name] [phone], " \
                   "phone [Name], delete [Name] [phone], show all, exit, good bye, close. "
        except Exception as error:
            return error
    return wrapper

@input_error
def hello():
    """
    Bot answer on "hello"
    :return: answer = string
    """
    return "How can I help you?"

@input_error
def add(user_input):
    '''
    Command for adding records to the dictionary
    :param command: user input
    :return: string
    '''

    name, phones = define_text(user_input)
    birthday = None

    for item in phones:
        bd = search(r"\b\d{2}[.]\d{2}[.]\d{4}", item)
        if bd:
            birthday = bd.group()
            phones.remove(birthday)

    if name not in ADDRESS_BOOK.data.keys():
        ADDRESS_BOOK.add_record(Record(name))
        if phones:
            for phone in phones:
                if phone not in ADDRESS_BOOK[name].get_phones():
                    ADDRESS_BOOK[name].add_phone(phone)
            if birthday:
                ADDRESS_BOOK[name].birthday = Birthday(birthday)
                return f"phones:[{', '.join(phones)}] and birthday: [{birthday}] were added to {name}"

            return f"{', '.join(phones)} was added to {name}"
    else:
        if phones:
            for phone in phones:
                if phone not in ADDRESS_BOOK[name].get_phones():
                    ADDRESS_BOOK[name].add_phone(phone)
            if birthday:
                ADDRESS_BOOK[name].birthday = Birthday(birthday)
                return f"phones:[{', '.join(phones)}] and birthday: [{birthday}] were added to {name}"
            return f"{', '.join(phones)} was added to {name}"


@input_error
def change(user_input):
    """
    Command for changing dictionary records
    :param text: user input
    :return: change the phone number of the user
    """

    name, phones = define_text(user_input)
    old_phone = int(phones[0])
    new_phone = int(phones[1])

    if name in ADDRESS_BOOK.data.keys():
        ADDRESS_BOOK[name].change_phone(old_phone, new_phone)
        return f"{name}`s phone is changed from {old_phone} to {new_phone}"
    else:
        raise KeyError(f"No records with '{name}' name found. Type another name to change")


@input_error
def phone(user_input):
    """
    Command for getting phone number of requested user
    :param text: user input
    :return: return phone number of requested user
    """

    name, phone = define_text(user_input)

    if name in ADDRESS_BOOK.data.keys():
        name_phones = list(map(lambda x: str(x), ADDRESS_BOOK[name].get_phones()))
        return f"{name}`s phones numbers are {', '.join(name_phones)}"
    else:
        raise KeyError(f"No records with '{name}' name found. Type another name to find")


@input_error
def delete_phone(user_input):
    """
    Command for deleting the phone number for the specified contact.
    :param text: user input
    :return: return message that phone number of requested user is deleted
    """
    name, phone = define_text(user_input)
    phone = phone[0]

    if phone in ADDRESS_BOOK[name].get_phones():
        ADDRESS_BOOK[name].delete_phone(phone)
        return f"{name}`s phone number '{phone}' was deleted"
    else:
        return f"{name} have no such phone number '{phone}'"


@input_error
def pagination(user_input):
    """
    Command for displaying the entered number of records.
    :param text: user input
    :return: return requested number of records
    """
    user_input = user_input.strip()

    if user_input:
        ADDRESS_BOOK.to_index = ADDRESS_BOOK.from_index + int(user_input)
        ADDRESS_BOOK.pagination = int(user_input)

    contacts = next(ADDRESS_BOOK)
    if contacts:
        page = ""
        for item in contacts:
            page += f"{item} - Phones:[{ADDRESS_BOOK[item].get_phones()}], Birthdays:[{ADDRESS_BOOK[item].birthday}]\n"
        return page
    else:
        return "You reach the end of a list. Start again?"


@input_error
def show_all():
    """
    Command for showing all dictionary records
    :return: All existed Address Book records
    """
    records = ''
    if ADDRESS_BOOK.data:
        records += 'Address book records are:\n'
        for name in ADDRESS_BOOK.data:
            records += f"{name}: {ADDRESS_BOOK[name].get_phones()}, Birthday:{ADDRESS_BOOK[name].birthday}\n"
        return records
    else:
        return "The Address Book is empty"


@input_error
def show_birthday(user_input):
    """
    Command for showing number of days to the next birthday
    :return: number of days
    """
    name, phone = define_text(user_input)

    if ADDRESS_BOOK[name].birthday:
        return f"{name}`s birthday is {ADDRESS_BOOK[name].birthday} it`s {ADDRESS_BOOK[name].days_to_birthday()} days " \
               f"left to the birthday "
    else:
        return "There is no information"


@input_error
def exit():
    """
    "good bye", "close", "exit" on any of these commands,
    the bot terminates its work after it displays "Good bye!" in the console.
    :return: string
    """
    return "Good bye!"


# Bot commands with associated functions
COMMANDS = {
    'hello': hello,
    'exit': exit,
    'close': exit,
    'good bye': exit,
    'add': add,
    'change': change,
    'delete': delete_phone,
    'show all': show_all,
    'phone': phone,
    'pagination': pagination,
    'birthday': show_birthday
}


def define_text(user_input):
    """
    Split command data to command, name, phones
    :param command: user_input
    :return: split data
    """

    result = user_input.lower().strip().split()

    name = result[0].capitalize()
    phones = result[1:]

    if name.isdigit():
        raise ValueError('Please enter valid contact name.')

    # if phones:
    #     for number in phones:
    #         if not number.isnumericdigit():
    #             raise ValueError('Please enter valid phone number.')

    return name, phones


def incorrect_command():
    """
    Incorrect command input
    :return: Message error
    """
    return "No command found. Please type one of this: hello, add [Name] [phone1] [phone2]...[birthday], " \
           "change [Name] [old_phone] [new_phone], phone [Name], delete [Name] [phone], birthday [Name], " \
           "pagination [page], show all, exit, good bye, close. "


def main(name: str):
    '''
    A console bot assistant that recognizes commands entered from the keyboard and responds according to the entered command.
    :param name: name of the Bot
    :return: Answers according to commands
    '''

    print(f'Hello! I\'m {name}. Your bot-assistant.')

    # Bot execution
    while True:
        command = input('User typing: ')
        command_new = command.lower().strip()
        command_data = ''
        for key in COMMANDS:
            if command.startswith(key):
                command_new = key
                command_data = command[len(key):]
                break

        if command_data:
            result = COMMANDS.get(command_new, incorrect_command)(command_data)
        else:
            result = COMMANDS.get(command_new, incorrect_command)()

        if result == 'How can I help you?':
            print(result)
        elif result == "Good bye!":
            print(result)
            break
        else:
            print(result)
            print('Anything else?')

if __name__ == "__main__":
    main('Bob')