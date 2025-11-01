p = input('Digite uma palavra:  ')
soma = 0
for l in p :
    if l == 'a':
        soma = soma + 1
        print('     ',l, 'é uma vogal.')
    elif l == 'e':
        soma = soma + 1
        print('     ',l, 'é uma vogal.')
    elif l == 'i':
        soma = soma + 1
        print('     ',l, 'é uma vogal.')
    elif l == 'o':
        soma = soma + 1
        print('     ',l, 'é uma vogal.')
    elif l == 'u':
        soma = soma + 1
        print('     ',l, 'é uma vogal.')
    else:
        print('     ',l,'Não é vogal')
    
print('    A palavra  ', p, 'tem ',soma, 'vogais')