def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ValueError:
            return 'Entered phone value must be integer'
        except KeyError:
            return 'No records with such key found'
    return wrapper

@input_error
def main(name: str):
    '''
    A console bot assistant that recognizes commands entered from the keyboard and responds according to the entered command.
    :param name: name of the Bot
    :return: Answers according to commands
    '''

    print(f'Hello! I\'m {name}. Your bot-assistant.')

    # dictionary for username and telephone records
    users_tel_book = {}

    # user inputs
    def user_input():
        command = input('Type: ')
        return command

    command = user_input()

    # command for adding records to the dictionary
    def add(command: str, users_tel_book):
        if not users_tel_book.get(command.split()[1]):
            if command.split()[2].isdigit():
                users_tel_book[command.split()[1]] = command.split()[2]
                print(f"The phone number of the '{command.split()[1]}' has recorded as '{command.split()[2]}'")
                print('Anything else?')
            else:
                print(f"Entered phone value '{command.split()[2]}' must be integer")
        else:
            print(f"'{command.split()[1]}' name has already existed. It can't be changed by command 'add'")

    # command for changing dictionary records
    def change(command: str, users_tel_book):
        if users_tel_book.get(command.split()[1]):
            if command.split()[2].isdigit():
                users_tel_book[command.split()[1]] = command.split()[2]
                print(f"The phone number of the '{command.split()[1]}' is changed to '{command.split()[2]}'")
                print('Anything else?')
            else:
                print(f"Entered phone value '{command.split()[2]}' must be integer")
        else:
            print(f"No records with '{command.split()[1]}' name found. Type another name to change")

    # command for getting telephone of requested user
    def phone(command: str, users_tel_book):
        if users_tel_book.get(command.split()[1]):
            print(f"The phone number of the '{command.split()[1]}' is '{users_tel_book.get(command.split()[1])}'")
            print('Anything else?')
        else:
            print(f"No records with '{command.split()[1]}' name found. Type another name to find")

    # command for showing all dictionary records
    def show_all(users_tel_book):
        if users_tel_book != {}:
            print(f'The list of users is: ')
            for user, phone in users_tel_book.items():
                print(f"{user}: {phone}")
            print('Anything else?')
        else:
            print(f"The list of users is empty")

    # Bot execution
    while command:
        if command == 'hello':
            print("How can I help you?")
        elif 'add' in command.split():
            add(command, users_tel_book)
        elif 'change' in command.split():
            change(command, users_tel_book)
        elif 'phone' in command.split():
            phone(command, users_tel_book)
        elif command == 'show all':
            show_all(users_tel_book)
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print(f"No '{command}' command found. Please type one of this: hello, add [Name] [phone], change [Name] ["
                  f"phone], phone [Name], show all, exit, good bye, close.")
        command = user_input()

if __name__ == "__main__":
    main('Bob')