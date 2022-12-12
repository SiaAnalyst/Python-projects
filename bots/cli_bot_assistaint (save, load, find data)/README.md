### CLI bot assistant (save data to file, load data from the file, search content)

#### In this project:
- Added functionality to save address book to disk and restore from disk. To do this, `JSON` protocol of data serialization/deserialization was selected and methods were implemented that will allow you to save all data to a file and load it from a file.
- Added the ability for the user to search the contents of the contact book, so that you can find all the information about one or more users by a few digits of the phone number or letters of the name, etc.

#### Acceptance criteria:
- The program does not lose data after exiting the program and restores it from the file.
- The program displays a list of users who have a match in their name or phone number with the entered string.