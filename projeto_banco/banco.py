contas = [{
    'nome': 'Eliseu',
    'cpf_cnpj': '123.456.789-10',
    'tipo_conta': 'p',
    'saldo': 500,
    'senha': 123456
},{
    'nome': 'Elias',
    'cpf_cnpj': '12.345.678/0001-10',
    'tipo_conta': 'j',
    'saldo': 300,
    'senha': 123457
}]

opcao = 0

def login():

    print('C: corrente, P: poupança, S: salário, J: jurídica')
    tipo = input('Informe o tipo de conta: ')

    tipo_formatado = tipo.lower()

    if tipo_formatado == 'j':
        login = input('Informe o CNPJ, apenas números: ')
        login_formatado = f'{login[0:2]}.{login[2:5]}.{login[5:8]}/{login[8:12]}-{login[12:14]}'
        
    else:
        login = input('Informe seu CPF, apenas números: ')
        login_formatado = f'{login[0:3]}.{login[3:6]}.{login[6:9]}-{login[9:11]}'
        
    
    for conta in contas:

        if conta['cpf_cnpj']  == login_formatado:
            
            contador = 3

            senha = int(input(f"Olá {conta['nome']}, informe sua senha: "))


            while contador != 1:

                contador -= 1

                if conta['senha'] == senha:
                    print('Login realizado com sucesso!')
                    return conta 
                else:
                    senha = int(input(f"Senha incorreta! Tente novamente. Lembrando, você só tem {contador} chances. "))
        
        

def transferir(conta):

    conta_destino = input('Digite o cpf ou cnpj da conta destino: ')
    vlr = float(input('Digite o valor que você quer transferir: '))

    if vlr < conta['saldo']:
        if len(conta_destino) == 11:

            conta_destino_formatado = f'{conta_destino[0:3]}.{conta_destino[3:6]}.{conta_destino[6:9]}-{conta_destino[9:11]}'
        
        else:

            conta_destino_formatado = f'{conta_destino[0:2]}.{conta_destino[2:5]}.{conta_destino[5:8]}/{conta_destino[8:12]}-{conta_destino[12:14]}'
        
        print(conta_destino_formatado)


        for destino in contas:
            if conta_destino_formatado == destino['cpf_cnpj']:
                conta['saldo'] -= vlr
                destino['saldo'] += vlr

        
            
        print("__________Tranzação realizada com sucesso!_________")
        print(f"Origem: {conta['nome']} CPF: {conta['cpf_cnpj']}  Saldo: {conta['saldo']}")
        print(f"Destino: {conta_destino_formatado['nome']} CPF: {conta_destino_formatado['cpf_cnpj']}  Saldo: {conta_destino_formatado['saldo']}")
    else:
        print('Saldo insuficiente.')

                
def depositar(vlr, conta):

    conta['saldo'] += vlr

def cadastro(nome, cpf, tipo, senha):

    conta = {
        'nome': nome,
        'cpf_cnpj': cpf,
        'tipo_conta': tipo,
        'saldo': 0,
        'senha': senha
    }

    contas.append(conta)

    print('Cadastro realizado com sucesso!')

    print(contas)
        

while True:

    print('________Sistema Bancário________')
    print('1: Fazer login')
    print('0: Sair')

    opcao = int(input())


    if opcao == 0:
        print('Você saiu do sistema bancario!')
        break
    elif opcao == 1:
        print('_________login_________')
        conta = login()

        opcao = 0

        while True:

            print('1: Depositar')
            print('2: Transferir')
            print('0: Sair')
            opcao = int(input('Escolha uma das opcões: '))

            if opcao == 0:
                print('Você saiu da conta.')
                break

            elif opcao == 1:
                print('__________Depositar__________')
                vlr = float(input(f"{conta['nome']}, digite o valor do deposito: "))
                depositar(vlr, conta)
                print(conta)

            elif opcao == 2:
                print('Transferir')
                transferir(conta)

    elif opcao == 3:
        print(contas)
    else:
        print('Opção incorreta.')