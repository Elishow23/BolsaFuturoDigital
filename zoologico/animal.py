class Animal:
    def __init__(self, nome, idade, alimentacao):
        # O prefixo __ (duplo underscore) torna os atributos privados
        self.__nome = nome
        self.__idade = idade
        self.__alimentacao = alimentacao

    # --- Métodos para o NOME ---
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str):
            self.__nome = valor
        else:
            print("Erro: O nome deve ser uma string.")

    # --- Métodos para a IDADE ---
    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, valor):
        if valor >= 0:
            self.__idade = valor
        else:
            print("Erro: A idade não pode ser negativa.")

    # --- Métodos para a ALIMENTACAO ---
    @property
    def alimentacao(self):
        return self.__alimentacao

    @alimentacao.setter
    def alimentacao(self, valor):
        self.__alimentacao = valor

    def exibir_info(self):
        print(f"Animal: {self.nome} | Idade: {self.idade} | Dieta: {self.alimentacao}")

    # --- Métodos para emitir som ---
    @property
    def emitir_som(self):
        return self.__emitir_som

    def exibir_info(self):
        # Usamos os getters da classe pai para acessar os dados privados
        print(f"Mamífero: {self.nome} | Gestação: {self.tempo_gestacao} meses | Dieta: {self.alimentacao}")

    # Método específico
    def amamentar(self):
        print(f"O mamífero {self.nome} está amamentando seus filhotes.")