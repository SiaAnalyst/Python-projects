import telebot

bot = telebot.TeleBot('')

users_tel_book = {}


@bot.message_handler(commands=['start'])
def start(message):
    message_to_user = f"Hello, {message.from_user.first_name}! I'm Bob. Your bot-assistant."
    bot.send_message(message.chat.id, message_to_user)


@bot.message_handler()
def get_user_text(message):
    if message.text == 'hello':
        bot.send_message(message.chat.id, "How can I help you?")
    elif 'add' in message.text.split():
        add(message)
    elif 'change' in message.text.split():
        change(message)
    elif 'phone' in message.text.split():
        phone(message)
    elif message.text == 'show all':
        show_all(message)
    elif message.text in ["good bye", "close", "exit"]:
        exit(message)
    else:
        message_to_user = f"No '{message.text}' command found. Please type one of this: hello, add [Name] [phone], change " \
                          f"[Name] [phone], phone [Name], show all, exit, good bye, close. "
        bot.send_message(message.chat.id, message_to_user)


# command for adding records to the dictionary
#@bot.message_handler(commands=['add'])
def add(message):
    message_text = message.text.split()
    name = message_text[1]
    phone = message_text[2]

    if not users_tel_book.get(name):
        if phone.isdigit():
            users_tel_book[name] = phone
            message_to_user = f"The phone number of the '{name}' has recorded as '{phone}'"
            bot.send_message(message.chat.id, message_to_user)
            bot.send_message(message.chat.id, "Anything else?")
        else:
            message_to_user = f"Entered phone value '{phone}' must be integer"
            bot.send_message(message.chat.id, message_to_user)
    else:
        message_to_user = f"'{name}' name has already existed. It can't be changed by command 'add'"
        bot.send_message(message.chat.id, message_to_user)


# command for changing dictionary records
#@bot.message_handler(commands=['change'])
def change(message):
    message_text = message.text.split()
    name = message_text[1]
    phone = message_text[2]

    if users_tel_book.get(name):
        if phone.isdigit():
            users_tel_book[name] = phone
            message_to_user = f"The phone number of the '{name}' is changed to '{phone}'"
            bot.send_message(message.chat.id, message_to_user)
            bot.send_message(message.chat.id, "Anything else?")
        else:
            message_to_user = f"Entered phone value '{phone}' must be integer"
            bot.send_message(message.chat.id, message_to_user)
    else:
        message_to_user = f"No records with '{name}' name found. Type another name to change"
        bot.send_message(message.chat.id, message_to_user)


# command for getting telephone of requested user
#@bot.message_handler(commands=['phone'])
def phone(message):
    message_text = message.text.split()
    name = message_text[1]

    if users_tel_book.get(name):
        message_to_user = f"The phone number of the '{name}' is '{users_tel_book.get(name)}'"
        bot.send_message(message.chat.id, message_to_user)
    else:
        message_to_user = f"No records with '{name}' name found. Type another name to find"
        bot.send_message(message.chat.id, message_to_user)


# command for showing all dictionary records
#@bot.message_handler(commands=['show all'])
def show_all(message):
    if users_tel_book != {}:
        bot.send_message(message.chat.id, f"The list of users is: ")
        for user, phone in users_tel_book.items():
            bot.send_message(message.chat.id, f"{user}: {phone}")
    else:
        bot.send_message(message.chat.id, f"The list of users is empty")
    bot.send_message(message.chat.id, 'Anything else?')


# command to exit
#@bot.message_handler(commands=['exit', 'close', 'good bye'])
def exit(message):
    bot.send_message(message.chat.id, "Good bye!")


bot.polling()
