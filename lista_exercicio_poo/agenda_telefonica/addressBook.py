class AddressBook:

    def __init__(self):
        self.contacts = [
            {"id": 1, "nome": "Eliseu Cosme", "telefone": "71 99999-0001", "email": "eliseu@email.com"},
    {"id": 2, "nome": "Ana Silva", "telefone": "11 98888-1111", "email": "ana.silva@provedor.com"},
    {"id": 3, "nome": "Bruno Oliveira", "telefone": "21 97777-2222", "email": "bruno.oli@web.com"},
    {"id": 4, "nome": "Carla Souza", "telefone": "31 96666-3333", "email": "carla.souza@empresa.com"},
    {"id": 5, "nome": "Diego Santos", "telefone": "85 95555-4444", "email": "diego.santos@gmail.com"},
    {"id": 6, "nome": "Fernanda Lima", "telefone": "41 94444-5555", "email": "fer.lima@uol.com"},
    {"id": 7, "nome": "Gabriel Costa", "telefone": "19 93333-6666", "email": "gabriel.costa@tech.com"},
    {"id": 8, "nome": "Helena Matos", "telefone": "27 92222-7777", "email": "helena.matos@ig.com"},
    {"id": 9, "nome": "Igor Pereira", "telefone": "48 91111-8888", "email": "igor.p@outlook.com"},
    {"id": 10, "nome": "Juliana Rocha", "telefone": "62 90000-9999", "email": "ju.rocha@gmail.com"}
        ]

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