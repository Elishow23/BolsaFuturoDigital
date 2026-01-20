class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number):
            contact = {'name': name, 'phone_number': phone_number}
            self.contacts.append(contact)

    def remove_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact['name'] != name]

    def find_contact(self, name):
        for contact in self.contacts:
            if contact['name'] == name:
                return contact
        return None

    def list_contacts(self):
        for contact in self.contacts:
            print(f"Nome: {contact['name']}, Telefone: {contact['phone_number']}")
