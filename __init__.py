from field import Name, Phone
from record import Record
from address_book import AddressBook

# Create an address book instance


# Creation of an entry for John

name_str = "John"
name = Name(name_str)
john_record = Record(name)

phone = Phone("1234567890")
john_phone = Phone("5555555555")
john_record.add_phone(phone)
john_record.add_phone(john_phone)

print(name.value)

# Add a John entry to the address book

book = AddressBook()
book.add_record(john_record)

# Creating and adding a new entry for Jane
name2 = Name("Jane")
jane_record = Record(name2)
Phone1 = Phone("9876543210")
jane_record.add_phone(Phone1)
book.add_record(jane_record)

# Displaying all entries in the contact list
for name, record in book.data.items():
    print(record)

    # Find and edit a phone number for John
print()
phone2 = Phone("1112223333")
john = book.find(name)
print(john)
john.edit_phone(john_record.phones[0], phone2)

# Displaying: Contact name: John, phones: 1112223333; 5555555555

# Searching for a specific phone number in John's entry
found_phone = john.find_phone(john_record.phones[1])
print(f"{john.name.value}: {found_phone}")
    # Deletion: 5555555555

    # Deletion Jane's entry
book.delete(name2)