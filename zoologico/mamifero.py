from animal import Animal

class Mamifero(Animal):
    def __init__(self, nome, idade, alimentacao, tempo_gestacao):
        super().__init__(nome, idade, alimentacao)
        self.__tempo_gestacao = tempo_gestacao

    @property
    def tempo_gestacao(self):
        return self.__tempo_gestacao

    @tempo_gestacao.setter
    def tempo_gestacao(self, valor):
        if valor > 0:
            self.__tempo_gestacao = valor
        else:
            print("Erro: Tempo de gestação deve ser positivo.")
            
    def exibir_info(self):
    # Usamos self.tempo_gestacao (sem __) para chamar a property acima
        print(f"Mamífero: {self.nome} | Gestação: {self.tempo_gestacao} meses | Alimentação: {self.alimentacao} | Idade: {self.idade}")
        
    def amamentar(self):
        print(f'O {self.nome} está amamentando')