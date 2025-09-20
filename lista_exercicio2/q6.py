senha = input('Digite a senha: ')
ten = 1

while senha != 'abc123' and ten != 3:
    ten += 1
    senha = input(print('Senha incorreta, digite a senha novamente: '))

if senha == 'abc123':
    print('Acesso permitido')
else:
    print('Acesso bloqueado')