from collections import UserDict


class Field:
    """
    `Field` class, which is the parent for all fields,
    and is responsible for the logic common to all fields.
    """
    def __init__(self, value):
        self.value = value


class Name(Field):
    """
    `Name` class, a mandatory field with a name.
    """
    pass


class Phone(Field):
    """
    `Phone` class, an optional field with a phone number
    and such one record (`Record`) can contain several.
    """
    pass


class Record:
    """
    `Record` class, which is responsible for the logic of
    adding/deleting/editing optional fields and storing the required field Name.
    """

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def change_phone(self, phone, new_phone):
        for item in self.phones:
            if item.value == phone:
                item.value = new_phone

    def delete_phone(self, phone):
        for item in self.phones:
            if item.value == phone:
                self.phones.remove(item)

    def get_phones(self):
        all_phones = [phone.value for phone in self.phones]
        return all_phones


class AddressBook(UserDict):
    """
    `AddressBook` class, which is inherited from `UserDict`,
    and is responsible for the logic of searching for records in this class.
    """
    def add_record(self, record):
        self.data[record.name.value] = record


if __name__ == '__main__':
    address_book = AddressBook()
    name = Name('Marry')
    phone = Phone('+380961111111')
    record = Record(name, phone)
    address_book.add_record(record)
    record.change_phone(phone, Phone('+380932222222'))
    record.add_phone(Phone('+380963333333'))
    print(address_book.keys())
    print(record.get_phones())