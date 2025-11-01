import usuario as us

class pac(us.usuario):
    def __init__(self, nome, cpf, senha, medico, quarto, acompanhante):
        super().__init__(nome, cpf) #herda atributos de Usuario
        self.__senha = None #atributo privado da subclasse
        self.__medico = None
        self.__quarto = None
        self.__acompanhante = None
        
    #getter
    
    def senha_pac(self):
        return self.__senha
    
    def medico_pac(self):
        return self.__medico
    
    def quarto_pac(self):
        return self.__quarto
    
    def acompanhante_pac(self):
        return self.__acompanhante
    
    #Setter
    
    def senha_pac(self, nova_senha):
        self.__senha = nova_senha
        
    def apresentar(self):
        print(f'Olá, paciente {self.nome_paciente}, seja bem-vindo!')
        
    