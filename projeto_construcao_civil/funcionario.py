# CÓDIGO COMPLETO EM CÉLULA ÚNICA
# Gerenciador de Obras com POO (v. Diário de Obra)

# Importações para limpar a tela, usar datas e gerar gráficos

import datetime


# -----------------------------------------------------------------
# CLASSE FUNCIONARIO (COM LOCALIZAÇÃO)
# -----------------------------------------------------------------

class Funcionario:
    """
    Representa um funcionário da obra.
    Localização é definida na criação.
    """
    def __init__(self, id_funcionario, nome, funcao, telefone, localizacao_inicial):
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.funcao = funcao
        self.telefone = telefone
        self.data_contratacao = datetime.date.today().strftime('%d/%m/%Y')
        self.localizacao = localizacao_inicial
        self.etapas_designadas = []

    def adicionar_etapa(self, etapa):
        """ Designa uma etapa para este funcionário """
        if etapa not in self.etapas_designadas:
            self.etapas_designadas.append(etapa)

    def atualizar_localizacao(self, nova_localizacao):
        """ Método para atualizar a localização do funcionário na obra """
        self.localizacao = nova_localizacao
        print(f"Localização de {self.nome} atualizada para: {self.localizacao}")

    def mostrar_info(self):
        """ Mostra os dados DETALHADOS do funcionário """
        print(f"\n--- Detalhes do Funcionário ID: {self.id_funcionario} ---")
        print(f"Nome: {self.nome}")
        print(f"Função: {self.funcao}")
        print(f"Telefone: {self.telefone}")
        print(f"Data de Contratação: {self.data_contratacao}")
        print(f"Localização Atual: {self.localizacao}")
        print(f"Total de Etapas Designadas: {len(self.etapas_designadas)}")

    def listar_etapas_do_funcionario(self):
        """
        Lista de Etapas por Membro (Listagem Completa)
        """
        print(f"\n--- Etapas de {self.nome} (ID: {self.id_funcionario}) ---")
        if not self.etapas_designadas:
            print("Nenhuma etapa designada.")
        else:
            for etapa in self.etapas_designadas:
                etapa.exibir_detalhes()