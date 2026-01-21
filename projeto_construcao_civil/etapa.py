from funcionario import Funcionario

# -----------------------------------------------------------------
# CLASSE ETAPA (BASE)
# -----------------------------------------------------------------

class Etapa:
    """
    Classe base para uma Etapa da Obra.
    Demonstra Encapsulamento.
    """
    def __init__(self, titulo, descricao, data_entrega):
        self.titulo = titulo
        self.descricao = descricao
        self.data_entrega = data_entrega
        self.status = "Pendente"
        self.responsavel = None

    def designar_responsavel(self, funcionario):
        """ Designação de Tarefas (Etapas) """
        if isinstance(funcionario, Funcionario):
            self.responsavel = funcionario
            funcionario.adicionar_etapa(self)
            print(f"Etapa '{self.titulo}' designada para {funcionario.nome}.")
        else:
            print("Erro: Só é possível designar para um Funcionario.")

    def atualizar_status(self, novo_status):
        """ Gestão de Status """
        if novo_status in ["Pendente", "Em andamento", "Concluída"]:
            self.status = novo_status
            print(f"Status da etapa '{self.titulo}' alterado para '{novo_status}'.")
        else:
            print(f"Erro: Status '{novo_status}' é inválido.")

    def exibir_detalhes(self):
        """
        Método base para Polimorfismo.
        As classes filhas vão sobrescrever este método.
        """
        resp = self.responsavel.nome if self.responsavel else "Ninguém"
        print(f"  [Etapa Padrão] {self.titulo} ({self.status})")
        print(f"    Descrição: {self.descricao}")
        print(f"    Responsável: {resp} | Entrega: {self.data_entrega}")
