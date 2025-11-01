idade = int(input('Informe a idade: '))

if idade >= 60:
    print('Idoso')
elif idade < 60 and idade >= 18:
    print('Adulto')
elif idade <= 17 and idade >= 12:
    print('Adolescente')
elif idade < 12:
    print('Criança')