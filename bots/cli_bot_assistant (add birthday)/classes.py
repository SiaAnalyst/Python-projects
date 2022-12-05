from collections import UserDict
from datetime import date, datetime
import re

class Field:
    """
    `Field` class, which is the parent for all fields,
    and is responsible for the logic common to all fields.
    """
    def __init__(self, value):
        self.__value = value
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class Name(Field):
    """
    `Name` class, a mandatory field with a name.
    """
    pass


class Birthday(Field):
    @Field.value.setter
    def value(self, value):
        if re.search(r"\b\d{2}[.]\d{2}[.]\d{4}", value):
            value_splited = value.split(".")
            self.__value = date(year=int(value_splited[2]), month=int(
                value_splited[1]), day=int(value_splited[0]))
        else:
            raise Exception("Birthday must be in DD.MM.YYYY format")

    def __str__(self) -> str:
        return self.__value.strftime("%d.%m.%Y")


class Phone(Field):
    """
    `Phone` class, an optional field with a phone number
    and such one record (`Record`) can contain several.
    """

    @Field.value.setter
    def value(self, value):
        analyze = re.search(r"\+380\d{9}\b", value)
        if analyze:
            self.__value = analyze.group()
        else:
            raise Exception("Phone must be in +380CCXXXXXXX format")


class Record:
    """
    `Record` class, which is responsible for the logic of
    adding/deleting/editing optional fields and storing the required field Name.
    """

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

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

    def days_to_birthday(self):
        if self.birthday:
            today = date.today()
            bd = datetime.strptime(self.birthday.value, "%d.%m.%Y").date().replace(year=today.year)
            if bd > today:
                return (bd - today).days
            else:
                return (bd.replace(year=today.year + 1) - today).days
        else:
            return None


class AddressBook(UserDict):
    """
    `AddressBook` class, which is inherited from `UserDict`,
    and is responsible for the logic of searching for records in this class.
    """

    def __init__(self):
        super().__init__()
        self.pagination = 1
        self.from_index = 0
        self.to_index = 1

    def add_record(self, record):
        self.data[record.name.value] = record

    def __next__(self):
        self.list_data = list(self.data.keys())  # keys
        if self.from_index >= len(self.list_data):
            self.from_index = 0
            self.to_index = self.pagination
        else:
            result = self.list_data[self.from_index:self.to_index]
            self.from_index += self.pagination
            self.to_index += self.pagination
            return result

    def __iter__(self):
        return self