class CaixaRegistradora:

    def __init__(self, id=0.0, saldo=0.0, qtdTransacao=0.0):
        self.__id = id
        self.__saldo = saldo
        self.__qtdTransacao = qtdTransacao
        self.historico = []

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @property
    def qtdTransacao(self):
        return self.__qtdTransacao
    
    @qtdTransacao.setter
    def qtdTransacao(self, qtdTransacao):
        self.__qtdTransacao = qtdTransacao

    def processarPagamento(self, valor):
        self.__saldo += valor
        self.__id += 1
        self.__qtdTransacao += 1

        id = self.__id

        t = {'id': id, 'tipo': 'pagamento', 'valor': valor}
        print(t)
        self.historico.append(t)

    def processarReembolso(self, id_transacao):
        for transacao in self.historico:
            if transacao['id'] == id_transacao:
                valor = transacao['valor']
                if valor <= self.__saldo:
                    self.__saldo -= valor
                    self.__id += 1

                    id = self.__id

                    t = {'id': id, 'tipo': 'reembolso', 'valor': valor}
                    print(t)
                    self.historico.append(t)
                    self.__qtdTransacao += 1
                    print(f'Reembolso de {valor} processado com sucesso.')
                else: 
                    print("Saldo insuficiente para reembolso.")

    def relatorio(self):
        print("\n--- RELATÓRIO DO DIA ---")
        if not self.historico:
            print("A agenda está vazia!")
            return
        
        for transacao in self.historico:
            print(f"ID: {transacao['id']}, Tipo: {transacao['tipo']}, Valor: {transacao['valor']}")
            
    def saldo(self):
        return print(self.__saldo)