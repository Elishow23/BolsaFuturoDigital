class Contact:

    def __init__(self, id, nome, telefone, email):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def displayInfo(self):
        return print(f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}")
    
    def updateContact(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email