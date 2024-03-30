from record import Record
from field import Name, Phone, Email
from datetime import datetime, timedelta
import pickle
from record import Record



class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: Name):
        if isinstance(name, str):
            name = Name(name)
            # Now proceed assuming 'name' is a Name object
        return self.data.get(name.value, None)

    def delete(self, name: Name):
        if name.value in self.data:
            del self.data[name.value]

    def get_birthdays_per_week(self):
        today = datetime.now()
        one_week_later = today + timedelta(days=7)
        names_to_congratulate = []

        for record in self.records.values():
            if record.birthday is not None:
                this_year_birthday = record.birthday.value.replace(year=today.year)
                if today <= this_year_birthday <= one_week_later:
                    names_to_congratulate.append(record.name.value)

        return names_to_congratulate


    def save_to_file(self, file_path):
        with open(file_path, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_from_file(file_path):
        with open(file_path, 'rb') as file:
            return pickle.load(file)
