import paciente as pac

pacientes = []
opcao = 0


while True:

  print('1: Cadastrar')
  print('2: Listar')
  print('3: Excluir')
  print('4: Sair')

  opcao = int(input('Informe uma opção: '))
 

  if opcao == 4:
    print('Você saiu do sistema, volte sempre!')
    break
  elif opcao == 1:
      
      
      paciente = pac.us('Eliseu', '078', '123', 'Elias', '22', 'Elisangela' )
    
      

    #paciente = {
    #    
    #    'nome': '',
    #    'medico': '',
    #    'quarto': '',
    #    'acompanhente': ''
    #}

    #print('Cadastro')

    #paciente['nome'] = input('Digite o nome do pacinete: ')
    #paciente['medico'] = input('Digite o nome do medico: ')
    #paciente['quarto'] = int(input('Digite numero do quarto do pacinete: '))
    #paciente['acompanhante'] = input('Digite o nome do acompanhante')

    #pacientes.append(paciente)

    #print('pacinete criado com sucesso!')
    
  elif opcao == 2:
    print(pacientes)
  
  elif opcao == 3:
    
    print(pacientes)
    excluir = input('Informe qual pacinete você quer excluir: ')

    for p in pacientes:

      if p['nome'] == excluir:
        pacientes.remove(p)

  else:
    print('Essa opção não existe')