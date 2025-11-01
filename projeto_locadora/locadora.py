from carro import Carro
#from cliente import Cliente

class Locadora:
    
    carros = {}
    
    def __init__ (self, lista_carro, lista_cliente):
        self.lista_carro = lista_carro
        self.lista_cliente = lista_cliente
        
    def cadastrar_carro(self):
        
        print('Cadastrar carro')
        
        carro1 = Carro('RND4G51', 'Chevrolet', 'Onix', 2019, True)
        
        return print(carro1)
        
    def cadastrar_cliente():
        print('Cadastrar cliente')
        
    def alugar_carro():
        print('Alugar carro')
        
    def devolver_carro():
        print('Devolver carro')
        
    def listar_carros_disponíveis():
        print('Listar carros disponiveis')
        
