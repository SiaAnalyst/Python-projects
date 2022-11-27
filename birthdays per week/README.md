### Get a list of colleagues who need to be congratulated
A useful function for displaying a list of colleagues who need to be congratulated on their birthdays during the week.

You have a list of dictionaries of users, each dictionary in it necessarily has keys name and birthday. This structure represents a model of a list of users with their names and birthdays. name is a string with the user's name, and birthday is a datetime object with the birthday.

The `get_birthdays_per_week` function receives a list of users as input and prints to the console (using print) a list of users to be congratulated by day.

`get_birthdays_per_week` outputs birthdays in the format:
- `Monday: Bill, Jill`
- `Friday: Kim, Jan`

Users whose birthday was on the weekend should be congratulated on Monday. The function displays users with birthdays a week ahead of the current day. The week starts on Monday.