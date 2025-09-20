usuario = input('Usuário: ')
senha = int(input('Senha: '))

if usuario == 'admin' and senha == 1234:
    print('Acesso permitido')
else:
    print('Acesso negado')