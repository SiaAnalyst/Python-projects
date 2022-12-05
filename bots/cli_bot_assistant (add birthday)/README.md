### CLI bot assistant (add Birthday)

#### In this project:
- Added a field for birthday `Birthday`. This field is optional, but there can be only one.
- Added functionality to work with `Birthday` in the `Record` class, namely the `days_to_birthday` function, which returns the number of days until the next birthday.
- Added functionality to check the correctness of the given values for the `Phone`, `Birthday` fields.
- Added pagination (page-by-page output) for `AddressBook` for situations when the book is very large and you need to show the contents in parts, not all at once. This is implemented by creating an iterator by records.

#### Acceptance criteria:
- `AddressBook` implements the `iterator` method, which returns a generator by `AddressBook` records and returns a view for `N` records in one iteration.
- `Record` class accepts one more additional (optional) argument of the `Birthday` class.
- `Record` class implements the `days_to_birthday` method, which returns the number of days until the next birthday of the contact, if the birthday is specified.
- `setter` and `getter` logic for the `value` attributes of `Field` class.
- Check for the correctness of the `setter` phone number for the `value` of the `Phone` class.
- Check for the correctness of the led birthday `setter` for the `value` of the `Birthday` class.