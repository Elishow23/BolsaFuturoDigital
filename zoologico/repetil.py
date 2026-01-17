from animal import Animal

class Reptil(Animal):
    def __init__(self, nome, idade, alimentacao, tipo_escamas):
        # Herança: enviando os dados básicos para a classe Animal
        super().__init__(nome, idade, alimentacao)
        # Atributo privado exclusivo de Répteis
        self.__tipo_escamas = tipo_escamas

    # Getter e Setter para tipo_escamas
    @property
    def tipo_escamas(self):
        return self.__tipo_escamas

    @tipo_escamas.setter
    def tipo_escamas(self, valor):
        self.__tipo_escamas = valor

    # Polimorfismo: Personalizando a exibição para Répteis
    def exibir_info(self):
        print(f"Réptil: {self.nome} | Escamas: {self.tipo_escamas} | Dieta: {self.alimentacao}")

    # Método exclusivo da classe Reptil
    def tomar_sol(self):
        print(f"{self.nome} está parado ao sol para aquecer seu sangue.")