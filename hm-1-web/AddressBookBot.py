import json
from datetime import datetime, timedelta
import pickle
from prettytable import PrettyTable

class Contact:
    def __init__(self, name, address, phone, email, birthday):
        self.name = name
        self.address = address
        self.__phone = phone
        self.__email = email
        try:
            datetime.strptime(birthday, "%Y-%m-%d")
            self.birthday = birthday
        except ValueError:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD' format for birthdays.")


    def to_dict(self):
        return {
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "email": self.email,
            "birthday": self.birthday
        }    

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if not isinstance(phone, str):
            raise ValueError("Phone number must be a string")
        if not phone.isdigit():
            raise ValueError("Phone number must contain only digits")
        if len(phone) != 10:
            raise ValueError("Phone number must be 10 digits long")
        self.__phone = phone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        exceptions = [";", ',', "[", "]", "*",
                      "(", ")", ">", "<", ":"]
        for i in exceptions:
            if email.find(i) != -1:
                raise ValueError("Mail contains prohibited characters")

        if "@" not in email and "." not in email:
            raise ValueError("Email must contain the @ symbol")
        if email[0] == "@" or email[-1] == "@":
            raise ValueError(
                "The @ symbol cannot be the first or last character")
        if email.count('@') > 1:
            raise ValueError("The @ symbol must be only one ")
        self.__email = email

    
class AddressBook:
    def __init__(self):
        self.contacts = []
    
    def search_contacts(self, search_term):
        results = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term.lower() in contact.phone.lower():
                results.append(contact)
        return results

    def edit_contact(self, old_name, new_name, new_email, new_phone, new_favorite):
        for contact in self.contacts:
            if contact.name == old_name:
                contact.name = new_name
                contact.email = new_email
                contact.phone = new_phone
                contact.favorite = new_favorite
                return True
        return False
    

    def get_upcoming_birthdays(self, days):
        today = datetime.now().date()
        upcoming_birthdays = []
        for contact in self.contacts:
            birthday = datetime.strptime(contact.birthday, "%Y-%m-%d").date()
            upcoming_birthday = birthday.replace(year=today.year)
            if today <= upcoming_birthday <= today + timedelta(days=days):
                upcoming_birthdays.append(contact)
        for contact in upcoming_birthdays:
            print(contact.to_dict())



    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return True
        return False

    def handle_hello():
        return "How can I help you?"

    def handle_add(self, name, address, phone, email, birthday):
        try:
            contact = Contact(name, address, phone, email, birthday)
            self.contacts.append(contact)
            return "Contact added successfully."
        except ValueError as e:
            return str(e)

    def handle_change(self, name, address, phone, email, birthday):
        for contact in self.contacts:
            if contact.name == name:
                try:
                    contact.address = address
                    contact.phone = phone
                    contact.email = email
                    contact.birthday = birthday
                    return "Contact updated successfully."
                except ValueError as e:
                    return str(e)
        return "Contact not found."

    def handle_delete(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return "Contact deleted successfully."
        return "Contact not found."

    def handle_search(self, search_term):
        results = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term.lower() in contact.phone.lower():
                results.append(contact)
        if results:
            return results
        else:
            return "No contacts found."

    def save_contacts(self, filename):
        with open(filename, "wb+") as file:
            pickle.dump(self.contacts, file)

    def load_contacts(self, filename):
        try:
           with open(filename, 'rb') as file:
             self.contacts = pickle.load(file)
        except FileNotFoundError:
                self.contacts = []

    def save_contacts2(self, filename):
        with open(filename, "w") as file:
            json.dump([contact.to_dict() for contact in self.contacts], file, indent=5, ensure_ascii=False)

    def load_contacts2(self, filename):
        try:
            with open(filename, "r" ) as file:
                contacts_data = json.load(file)
                self.contacts = [Contact(**data) for data in contacts_data]
        except FileNotFoundError:
            self.contacts = []            


def handle_add():
    name = input("Enter the name: ")
    address = input("Enter the address: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email: ")
    birthday = input("Enter the birthday (YYYY-MM-DD): ")

    result = AddressBookInstance.handle_add(name, address, phone, email, birthday)
    
    if result == "Contact added successfully.":
        AddressBookInstance.save_contacts("usersbook.pkl")
        AddressBookInstance.save_contacts2("usersbook.json")
        print(result)
    else:
        print("Error: " + result)


def handle_change():
    name = input("Enter the name of the contact to change: ")
    address = input("Enter the new address: ")
    phone = input("Enter the new phone number: ")
    email = input("Enter the new email: ")
    birthday = input("Enter the new birthday (YYYY-MM-DD): ")
    AddressBook.handle_change(name, address, phone, email, birthday)
    AddressBook.save_contacts("usersbook.pkl")
    AddressBook.save_contacts2("usersbook.json")
    print("Contact change successfully.") 


def handle_search():
    search_term = input("Enter the search term: ")
    results = AddressBook.handle_search(search_term)
    if isinstance(results, list):
        for contact in results:
            print(contact.to_dict())
    else:
        print(results)

def handle_delete():
    name = input("Enter the name of the contact to delete: ")
    result = AddressBook.handle_delete(name)
    if result:    
        AddressBook.save_contacts("usersbook.pkl")
        AddressBook.save_contacts2("usersbook.json")
        print("Contact delete successfully.") 
    else:
         print("Invalid note Name.")


def get_upcoming_birthdays():
    days = int(input("Enter the number of days to check: "))
    AddressBookInstance.get_upcoming_birthdays(days)


def save_contacts():
    filename = "usersbook.pkl"
    AddressBookInstance.save_contacts(filename)

def load_contacts():
    AddressBook.load_contacts("usersbook.pkl")

def save_contacts2():
    filename = "usersbook.json"
    AddressBookInstance.save_contacts2(filename)
    print("Contacts saved successfully json.")


def load_contacts2():
    AddressBook.load_contacts2("usersbook.json")
    print("Contacts loaded successfully json.")



from prettytable import PrettyTable

def main():
    global AddressBookInstance
    AddressBookInstance = AddressBook()
    AddressBookInstance.load_contacts2("usersbook.json")

    while True:
        menu = PrettyTable(["Option", "Description"])
        menu.add_rows([
            ["1", "Add a Contact"],
            ["2", "Change a Contact"],
            ["3", "Delete a Contact"],
            ["4", "Search Contact"],
            ["5", "Birthdays in the Coming Days"],
            ["6", "Close Contact"],
            ["7", "Save Contacts (pkl)"],
            ["8", "Load Contacts (pkl)"],
            ["9", "Save Contacts (json)"],
            ["10", "Load Contacts (json)"]
        ])
        print("-------Menu AddressBook:----")
        print(menu)

        command = input("Enter a command: ").lower()
        if command == "hello":
            print('I see You!!! Poot command)))))) ')

        elif command == "1":
            handle_add()

        elif command == "2":
            handle_change()

        elif command == "3":
            handle_delete()

        elif command == "4":
            handle_search()

        elif command == "7":
            save_contacts()
            print("Contacts saved successfully.")

        elif command == "8":
            load_contacts()
            print("Contacts loaded successfully.")

        elif command == "9":
            save_contacts2()
            print("Contacts saved in json format.")

        elif command == "10":
            load_contacts2()
            print("Contacts loaded from json format.")

        elif command == "5":
            get_upcoming_birthdays()

        elif command in ["good bye", "close", "exit", "6"]:
            save_contacts()
            print("-----Good bye!-----")
            break
        else:
            print("Invalid command.")
      


if __name__ == "__main__":
    main()