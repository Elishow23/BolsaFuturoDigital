class Contact:

    def __init__(self, id, nome, telefone, email):
        self.__id = id
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if len(novo_nome) > 0:
            self.__nome = novo_nome

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, novo_telefone):
        self.__telefone = novo_telefone

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, novo_email):
        self.__email = novo_email


    def displayInfo(self):
        return print(f"Nome: {self.__nome}, Telefone: {self.__telefone}, Email: {self.__email}")
    
    def updateContact(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email