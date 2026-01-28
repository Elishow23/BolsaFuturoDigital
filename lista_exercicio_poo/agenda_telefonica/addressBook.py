class AddressBook:

    def __init__(self):
        self.contacts = []

    def add_contact(self, id, nome, telefone, email):
            
            qtd_contato = len(self.contacts)

            if qtd_contato < 10:

                contato = {
                    'id': id,
                    'nome': nome,
                    'telefone': telefone,
                    'email': email
                }
                print(contato)
                self.contacts.append(contato)
                print('Contato adicionado com sucesso!')

            else:
                print('Ops, você já tem mais de 10 contatos')

    def list_contacts(self):
        if not self.contacts:
            print("A agenda está vazia!")
            return
            
        for contact in self.contacts:
            # Formatando a saída para ficar mais legível
            print(f"{contact['id']} - Nome: {contact['nome']} | Tel: {contact['telefone']} | Email: {contact['email']}")

    def update_contact(self, id, nome, telefone, email):
         for contact in self.contacts:
              if id == contact['id']:
                contact['nome'] = nome
                contact['telefone'] = telefone
                contact['email'] = email     
                print(f'usairio {contact['nome']} atualizado com sucesso!')

    def pesquisar(self, nome):
        resultado = []
        for contact in self.contacts:
            if nome == contact['nome']:
                resultado.append(contact)
        if not resultado:
            print('Contato não encontrado')
        
        for resultado in resultado:
            print(f'{resultado['id']}  - Nome: {resultado['nome']} | Telefone: {resultado['telefone']} | Email: {resultado['email']}')
        
    def deletar(self, id):
        for contact in self.contacts:
            if id == contact['id']:
                nome_removido = contact['nome']
                self.contacts.remove(contact)
                print(f"Contato {nome_removido} excluído com sucesso!")
                return
        
        print(f"Erro: ID {id} não encontrado.")