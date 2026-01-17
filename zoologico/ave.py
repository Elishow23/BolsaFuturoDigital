from animal import Animal

class Ave(Animal):
    def __init__(self, nome, idade, alimentacao, envergadura):
        super().__init__(nome, idade, alimentacao)
        self.__envergadura = envergadura

    @property
    def envergadura(self):
        return self.__envergadura
    
    @envergadura.setter
    def envergadura(self, valor):
        if valor > 0:
            self.__envergadura = valor
        else:
            print('Erro: A envergadura deve ser um valor positivo.')
        
    def exibir_info(self):
        print(f'Ave: {self.nome} | envergadura: {self.envergadura} | Dieta: {self.alimentacao} ')

    def voar(self):
        print(f'O(A) {self.nome} está batendo suas asas de {self.envergadura}m e voando!')