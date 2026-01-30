import caixa_registradora as CaixaRegistradora

opcao = 0

caixa = CaixaRegistradora.CaixaRegistradora()

while True:

    print('\n--- CAIXA REGISTRADORA ---')
    print('1 - Sair')
    print('2 - Realizar pagamento')
    print('3 - Realizar reembolso')
    print('4 - Relatório do dia')
    print('5 - Saldo atual')
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        print('Você saiu do sistema!')
        break
    elif opcao == 2:
        print('Realizar pagamento')
        valor = float(input('Digite o valor do pagamento:'))
        caixa.processarPagamento(valor)
    elif opcao == 3:
        print('Realizar reembolso')
        id_transacao = int(input('Digite o ID da transação para reembolso:'))
        caixa.processarReembolso(id_transacao)
    elif opcao == 4:
        print('Relatório do dia')
        caixa.relatorio()
    elif opcao == 5:
        print('Saldo atual"')
        caixa.saldo()
    else:
        print('Opção inválida! Tente novamente.') 