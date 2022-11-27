# User phone records
USER_CONTACTS = {}

# decorator to handle user input errors
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as value_error:
            return value_error
        except KeyError as key_error:
            return key_error
        except IndexError:
            return 'Please type: name and phone number'
        except TypeError:
            return "No command found. Please type one of this: hello, add [Name] [phone], change [Name] [phone], " \
                   "phone [Name], show all, exit, good bye, close. "
    return wrapper

@input_error
def hello():
    """
    Bot answer on "hello"
    :return: answer = string
    """
    return "How can I help you?"

@input_error
def add(message):
    '''
    Command for adding records to the dictionary
    :param command: user input
    :return: string
    '''

    name, phone = define_text(message)

    if not USER_CONTACTS.get(name):
        USER_CONTACTS[name] = phone
        return f"The phone number of the '{name}' has recorded as '{phone}'"
    else:
        raise KeyError(f"'{name}' name has already existed. It can't be changed by command 'add'")

@input_error
def change(message):
    """
    Command for changing dictionary records
    :param text: user input
    :return: change the phone number of the user
    """

    name, phone = define_text(message)

    if USER_CONTACTS.get(name):
        USER_CONTACTS[name] = phone
        return f"The phone number of the '{name}' is changed to '{phone}'"
    else:
        raise KeyError(f"No records with '{name}' name found. Type another name to change")

@input_error
def phone(user_input):
    """
    Command for getting phone number of requested user
    :param text: user input
    :return: return phone number of requested user
    """

    name = define_text(user_input)

    if USER_CONTACTS.get(name):
        return f"The phone number of the '{name}' is '{USER_CONTACTS.get(name)}'"
    else:
        raise KeyError(f"No records with '{name}' name found. Type another name to find")

@input_error
def show_all():
    '''
    Command for showing all dictionary records
    :return: All existed user contact records
    '''
    records = ''
    if USER_CONTACTS != {}:
        records += 'User contacts are:\n'
        for user, phone in USER_CONTACTS.items():
            records += f"{user}: {phone} \n"
        return records
    else:
        return "The list of users is empty"

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
    'show all': show_all,
    'phone': phone
}

def define_text(user_input):
    """
    Split command data to command, name, phone
    :param command: user_input
    :return: split data
    """

    result = user_input.lower().strip().split()

    name = result[0]
    phone = result[1]

    if name.isdigit():
        raise ValueError('Please enter valid name.')

    if not phone.isdigit():
        raise ValueError('Please enter valid phone number.')

    return name, phone


def incorrect_command():
    """
    Incorrect command input
    :return: Message error
    """
    return "No command found. Please type one of this: hello, add [Name] [phone], change [Name] [phone], " \
           "phone [Name], show all, exit, good bye, close. "


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