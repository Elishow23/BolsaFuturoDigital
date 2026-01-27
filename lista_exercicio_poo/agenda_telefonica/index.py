from contact import Contact
from addressBook import AddressBook

opcao = 10

a1 = AddressBook()

id = 0

while True:

    opcao = int(input('_____Menu_____\nDigite 0 para sair' \
    '\n1 para cadastrar contato\n2 para remover contato\n3 para consultar' \
    '\n4 pesquisar contato\n5 para atualizar contato: \n'))

    if opcao == 0:
        print('_____Saindo do sistema...')
        break
    elif opcao == 1:
        print('______Cadastrar contato______')

        id += 1
        nome = input('Digite o nome do contato: ')
        telefone = input('Digite o telefone do contato: ')
        email = input('Digite o email do contato: ')

        c = Contact(id, nome, telefone, email)
       
        c.displayInfo()
        a1.add_contact(c.id, c.nome, c.telefone, c.email)


    elif opcao == 2:
        print('______Remover contato______')
        id_referencia = int(input('Informe o id do contato a ser removido: '))
        a1.deletar(id_referencia)
    elif opcao == 3:
        print('______Consultar contatos______')
        a1.list_contacts()
    elif opcao == 4:
        print('_____Pesquisar contato_____')
        nome = input('Informe nome do contato: ')
        a1.pesquisar(nome)
    elif opcao == 5:
        print('_____Atualizar contato______')
        a1.list_contacts()
        id_referencia = int(input('Informe o ID do contato que irá ser atualizado: '))
        nome = input('Informe o novo nome: ')
        tele = input('Informe o novo telefone: ')
        email = input('Informe o novo email: ')
        a1.update_contact(id_referencia, nome, tele, email)
        a1.list_contacts()
       
    else:
        print('______Opção inexistente_______')

