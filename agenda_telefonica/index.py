from contact import Contact
from addressBook import AddressBook

opcao = 10

while True:

    opcao = int(input('Digite 0 para sair, 1 para cadastrar contato, 2 para remover contato, 3 para consultar: '))
    a1 = AddressBook()

    if opcao == 0:
        print('Saindo do sistema...')
        break
    elif opcao == 1:
        print('Cadastrar contato')
        c = Contact('Ana', '123456789', 'ana@gamil.com')
        c.displayInfo()
        a1.add_contact(c.name, c.phone)
    elif opcao == 2:
        print('Remover contato')
    elif opcao == 3:
        print('Consultar contatos')
        a1.list_contacts()
    else:
        print('Opção inexistente')

