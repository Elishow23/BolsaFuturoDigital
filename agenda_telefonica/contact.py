class Contact:

    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self, value):
        self.__phone = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    def displayInfo(self):
        return print(f"Nome: {self.__name}, Telefone: {self.__phone}, Email: {self.__email}")
    
    def updateContact(self, phone, email):
        self.__phone = phone
        self.__email = email