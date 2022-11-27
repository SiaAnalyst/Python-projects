### CLI bot assistant (using Classes)

In this project we will continue to develop our virtual assistant with CLI interface.

Our assistant is already able to interact with the user via the command line, receiving commands and arguments and performing the required actions. 
In this project, we worked on the internal logic of the assistant, on how the data is stored, what kind of data and what can be done with it. We used object-oriented programming for these purposes.

The user has an address book or contact book. This contact book contains records. Each record contains a certain set of fields.

The user interacts with the contact book by adding, deleting and editing entries. The user also has the ability to search for records in the contact book by one or more criteria (fields).

Fields can be either required (name) or optional (phone or email for example). Also records contain several fields of the same type (several phone numbers for example). The user can add/remove/edit fields in any record.

The following classes are implemented in this work:

- `AddressBook` class, which is inherited from `UserDict`, and is responsible for the logic of searching for records in this class.
- `Record` class, which is responsible for the logic of adding/deleting/editing optional fields and storing the required field Name.
- `Field` class, which is the parent for all fields, and is responsible for the logic common to all fields.
- `Name` class, a mandatory field with a name.
- `Phone` class, an optional field with a phone number and such one record (`Record`) can contain several.

`Record` records in `AddressBook` are stored as values in the dictionary. The `Record.name.value` is used as keys.
`Record` stores the `Name` object in a separate attribute.
`Record` stores a list of Phone objects in a separate attribute.
`Record` implements methods for adding/deleting/editing `Phone` objects.
`AddressBook` implements the `add_record` method, which adds a `Record` to `self.data`.