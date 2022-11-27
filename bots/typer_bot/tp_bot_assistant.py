import typer

app = typer.Typer()

@app.command()
def hello():
    users_tel_book = {}
    print(f'Hello! I\'m Bob. Your bot-assistant.')
    print("How can I help you?")
    return users_tel_book

# command for adding records to the dictionary
@app.command()
def add(name: str = typer.Argument(..., help='Name of user'),
        phone: int = typer.Argument(..., help='User phone number'),
        users_book = typer.Argument(users_tel_book, help='User phone number')):
    if not users_tel_book.get(name):
        users_tel_book[name] = phone
        print(users_tel_book)
        print('Done. Anything else?')
        return users_tel_book
    else:
        print(f"'{name}' name has already existed. It can't be changed by command 'add'")

# command for changing dictionary records
@app.command()
def change(name: str = typer.Argument(..., help='Name of user'), phone: int = typer.Argument(..., help='User phone number')):
    if users_tel_book.get(name):
        users_tel_book[name] = phone
        print('Done. Anything else?')
        return users_tel_book
    else:
        print(f"No records with '{name}' name found. Type another name to change")

# command for getting telephone of requested user
@app.command()
def phone(name: str = typer.Argument(..., help='Name of user')):
    if users_tel_book.get(name):
        print(f"{name}: {users_tel_book.get(name)}")
        print('Done. Anything else?')
        return users_tel_book
    else:
        print(f"No records with '{name}' name found. Type another name to find")

# command for showing all dictionary records
@app.command()
def show_all():
    print(users_tel_book)
    for user, phone in users_tel_book.items():
        print(f"{user}: {phone}")
    print('Done. Anything else?')

# command to exit
@app.command()
def exit():
    print("Good bye!")

# command to exit
@app.command()
def close():
    print("Good bye!")

# command to exit
@app.command()
def good_bye():
    print("Good bye!")

if __name__ == "__main__":
    app()