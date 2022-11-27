### CLI Bot assistant

Console bot assistant that recognizes commands entered from the keyboard and responds according to the entered command.

The bot assistant is a prototype of an assistant application. The assistant application in the first approximation is able to work with the contact book and calendar. The simplest and most convenient interface at the initial stage of development is the CLI (Command Line Interface) console application. CLI is quite simple to implement. Any CLI consists of three main elements:
- Command Parser. The part that is responsible for parsing strings entered by the user, selecting keywords and command modifiers from the string.
- Command handler functions - a set of functions, also called handler, they are responsible for the direct execution of commands.
- Request-response loop. This part of the program is responsible for receiving data from the user and returning a response to the user from the handler function.

At the first stage, our bot assistant is able to store the name and phone number, find the phone number by name, change the recorded phone number, display all the records that it has stored in the console. To implement such simple logic, we used a dictionary. In the dictionary we store the user name as a key and the phone number as a value.

The bot is in an infinite loop, waiting for the user's command.
The bot completes its work if it encounters the words: "good bye", "close", "exit".
The bot is not case-sensitive to the entered commands.
The bot accepts commands:
- `"hello"`, replies to the console "How can I help you?"
- `"add ..."`. At this command, the bot saves a new contact in memory (in the dictionary, for example). Instead of `...` the user enters the name and phone number, always separated by a space.
- `"change ..."` With this command, the bot saves a new phone number of an existing contact in memory. Instead of `...` the user enters the name and phone number, always separated by a space.
- `"phone ..."` At this command, the bot displays the phone number for the specified contact in the console. Instead of `...` the user enters the name of the contact whose number should be shown.
- `"show all"`. This command displays all saved contacts with phone numbers in the console.
- `"good bye", "close", "exit"` by any of these commands, the bot completes its work after it displays `"Good bye!"` in the console.
All user input errors are handled by the `input_error` decorator. This decorator is responsible for returning to the user messages such as "Enter user name", "Give me name and phone please", etc. The input_error decorator handles exceptions that occur in the handler functions (`KeyError`, `ValueError`, `IndexError`) and returns the appropriate response to the user.
Command logic is implemented in separate functions and these functions take one or more strings as input and return a string.
All the logic of interaction with the user is implemented in the main function, all print and input occur only there.