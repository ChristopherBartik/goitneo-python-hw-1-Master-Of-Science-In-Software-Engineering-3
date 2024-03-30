import address_book
from field import Name, Phone, Email
from record import Record
from datetime import datetime, timedelta
from address_book import AddressBook

# Create an address book instance

contacts = {}
def handle_command(command, args):
    if command == "add":
        name, phone, email = args.split(", ")
        record = Record(Name(name))
        if phone:
            record.add_phone(Phone(phone))
        if email:
            record.add_email(Email(email))
        address_book.AddressBook.add_record(record)
        return f"Added {name}."

    elif command == "change":
        # This example assumes changing a phone; similar logic for email or other fields
        name, old_phone, new_phone = args.split(", ")
        record = address_book.AddressBook.find(name)
        if record:
            record.remove_phone(Phone(old_phone))
            record.add_phone(Phone(new_phone))
            return f"Phone number changed for {name}."
        else:
            return "Contact not found."
    elif command == "phone":
        # Logic to display a contact's phone
    elif command == "all":
        return '\n'.join([f"{name}: {info['phone']}" for name, info in contacts.items()])


    elif command == "add-birthday":
        name, birthday_str = args.split(', ')
        birthday = datetime.strptime(birthday_str, "%Y-%m-%d")
        if name in contacts:
            contacts[name]['birthday'] = birthday
            return f"Added birthday for {name}."
        else:
            return "Contact not found."
    elif command == "show-birthday":
        name = args
        if name in contacts and 'birthday' in contacts[name]:
            return contacts[name]['birthday'].strftime("%Y-%m-%d")
        else:
            return "Birthday not found."
    elif command == "birthdays":
        today = datetime.now()
    upcoming_birthdays = []
    for name, info in contacts.items():
        if 'birthday' in info:
            next_birthday = info['birthday'].replace(year=today.year)
            if 0 <= (next_birthday - today).days < 7:
                upcoming_birthdays.append(name)
    return '\n'.join(upcoming_birthdays) if upcoming_birthdays else "No upcoming birthdays."
    elif command == "hello":
        return "Hello! How can I help you?"
    elif command in ["close", "exit"]:
        return "Goodbye!"
    else:
        return "Unknown command."