import re

from datetime import datetime, timedelta



class Birthday:

    def __init__(self, date):

        self.date = self.validate_birthday(date)



    def validate_birthday(self, date):

        try:

            validated_date = datetime.strptime(date, '%d.%m.%Y').date()

            return validated_date

        except ValueError:

            raise ValueError("Invalid birthday format. Use: DD.MM.YYYY")



class Record:

    def __init__(self, name, phone, birthday=None):

        self.name = name

        self.phone = self.validate_phone(phone)

        self.birthday = Birthday(birthday) if birthday else None



    def validate_phone(self, phone):

        phone_pattern = re.compile(r'^\d{10}$')

        if phone_pattern.match(phone):

            return phone

        else:

            raise ValueError("Invalid phone number. It should consist of 10 digits.")



class AddressBook:

    def __init__(self):

        self.contacts = []



    def add_contact(self, name, phone, birthday=None):

        contact = Record(name, phone, birthday)

        self.contacts.append(contact)

        return "Contact added."



    def change_contact(self, name, phone):

        for contact in self.contacts:

            if contact.name == name:

                contact.phone = phone

                return "Contact updated."

        return "Contact not found."



    def show_phone(self, name):

        for contact in self.contacts:

            if contact.name == name:

                return contact.phone

        return "Contact not found."



    def show_all(self):

        if not self.contacts:

            return "No contacts available."

        else:

            return "\n".join([f"{contact.name}: {contact.phone}" for contact in self.contacts])



    def add_birthday(self, name, birthday):

        for contact in self.contacts:

            if contact.name == name:

                contact.birthday = Birthday(birthday)

                return "Birthday added."

        return "Contact not found."



    def show_birthday(self, name):

        for contact in self.contacts:

            if contact.name == name and contact.birthday:

                return contact.birthday.date.strftime('%d.%m.%Y')

        return "Birthday not found."



    def get_birthdays_per_week(self):

        today = datetime.now().date()

        next_week_start = today + timedelta(days=(7 - today.weekday()))

        next_week_end = next_week_start + timedelta(days=6)



        upcoming_birthdays = []

        for contact in self.contacts:

            if contact.birthday:

                birthday_date = contact.birthday.date.replace(year=today.year)

                if next_week_start <= birthday_date <= next_week_end:

                    upcoming_birthdays.append((contact.name, birthday_date.strftime('%d.%m.%Y')))



        return upcoming_birthdays



def parse_input(user_input):

    cmd, *args = user_input.split()

    cmd = cmd.strip().lower()

    return cmd, args



def main():

    book = AddressBook()

    print("Welcome to the assistant bot!")



    while True:

        user_input = input("Enter a command: ")

        command, args = parse_input(user_input)



        if command in ["close", "exit"]:

            print("Good bye!")

            break

        elif command == "hello":

            print("How can I help you?")

        elif command == "add":

            print(book.add_contact(*args))

        elif command == "change":

            print(book.change_contact(*args))

        elif command == "phone":

            print(book.show_phone(*args))

        elif command == "all":

            print(book.show_all())

        elif command == "add-birthday":

            print(book.add_birthday(*args))

        elif command == "show-birthday":

            print(book.show_birthday(*args))

        elif command == "birthdays":

            birthdays = book.get_birthdays_per_week()

            if birthdays:

                print("Upcoming birthdays:")

                for name, date in birthdays:

                    print(f"{name}: {date}")

            else:

                print("No upcoming birthdays.")

        else:

            print("Invalid command.")



if __name__ == "__main__":

    main()