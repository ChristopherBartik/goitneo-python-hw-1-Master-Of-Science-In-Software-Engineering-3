from record import Record
from field import Name
from datetime import datetime, timedelta
import pickle


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

    def handle_command(command, args):
        if command == "add":
            # Logic to add a new contact
        elif command == "change":
            # Logic to change a contact's phone
        elif command == "phone":
            # Logic to display a contact's phone
        elif command == "all":
            # Logic to display all contacts
        elif command == "add-birthday":
            # Logic to add a birthday to a contact
        elif command == "show-birthday":
            # Logic to show a contact's birthday
        elif command == "birthdays":
            # Logic to show upcoming birthdays within the next week
        elif command == "hello":
            return "Hello! How can I help you?"
        elif command in ["close", "exit"]:
            # Logic to close the app
        else:
            return "Unknown command."

    def save_to_file(self, file_path):
        with open(file_path, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_from_file(file_path):
        with open(file_path, 'rb') as file:
            return pickle.load(file)
