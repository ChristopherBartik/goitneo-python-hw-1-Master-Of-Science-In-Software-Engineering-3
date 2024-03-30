from field import Name, Phone, Birthday, Email


class Record:
    def __init__(self, name: Name, birthday=None):
        self.name = name
        self.phones = []
        self.birthday = birthday

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def remove_phone(self, phone: Phone):
        self.phones = [p for p in self.phones if p.value != phone.value]

    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        for i, p in enumerate(self.phones):
            if p.value == old_phone.value:
                self.phones[i] = new_phone

    def find_phone(self, phone: Phone):
        return any(phone.value == p.value for p in self.phones)

    def add_birthday(self, birthday: Birthday):
        self.birthday = birthday

    def add_email(self, email: Email):
        self.emails.append(email)

    def __str__(self):
        phone_str = "; ".join(str(phone) for phone in self.phones)
        birthday_str = f", Birthday: {self.birthday.value}" if self.birthday else ""
        return f"Contact name: {self.name.value}, Phones: {phone_str}{birthday_str}"





