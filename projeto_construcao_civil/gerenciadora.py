import matplotlib.pyplot as plt
from IPython.display import clear_output


# -----------------------------------------------------------------
# CLASSE GERENCIADORA (OBRA)
# -----------------------------------------------------------------

class Obra:
    """ Gerencia a obra, funcionários e etapas """
    def __init__(self, nome_obra):
        self.nome_obra = nome_obra
        self.funcionarios = []
        self.etapas = []

    def adicionar_funcionario(self, funcionario):
        """ Adiciona um novo funcionário à obra """
        self.funcionarios.append(funcionario)
        print(f"Funcionário {funcionario.nome} (ID: {funcionario.id_funcionario}) adicionado à obra.")

    def adicionar_etapa(self, etapa):
        """ Adiciona uma nova etapa ao projeto """
        self.etapas.append(etapa)
        print(f"Etapa '{etapa.titulo}' adicionada à obra.")

    def mostrar_funcionarios(self):
        """ Lista todos os funcionários (resumido) - com localização """
        print(f"\n--- Funcionários da Obra {self.nome_obra} ---")
        if not self.funcionarios:
            print("Nenhum funcionário cadastrado.")
            return False

        for i, func in enumerate(self.funcionarios):
            print(f"  {i+1}. ID: {func.id_funcionario} | {func.nome} ({func.funcao}) | Local: {func.localizacao}")
        return True

    def mostrar_etapas(self):
        """ Lista todas as etapas, demonstrando Polimorfismo """
        print(f"\n--- Etapas da Obra {self.nome_obra} ---")
        if not self.etapas:
            print("Nenhuma etapa cadastrada.")
            return False

        for i, etapa in enumerate(self.etapas):
            print(f"\n  (Índice {i+1})")
            # AQUI OCORRE O POLIMORFISMO
            etapa.exibir_detalhes()
        return True

    def gerar_relatorio_progresso(self):
        """ Relatório de Progresso """
        print(f"\n--- Relatório de Progresso: {self.nome_obra} ---")
        if not self.etapas:
            print("Nenhuma etapa cadastrada.")
            return

        concluidas = 0
        pendentes_andamento = 0
        total = len(self.etapas)

        for etapa in self.etapas:
            if etapa.status == "Concluída":
                concluidas += 1
            else:
                pendentes_andamento += 1

        print(f"Total de Etapas: {total}")
        print(f"Etapas Concluídas: {concluidas}")
        print(f"Etapas Pendentes/Em Andamento: {pendentes_andamento}")
        print("---------------------------------")

    # --- NOVO MÉTODO: DIÁRIO DE OBRA ---
    def gerar_diario_obra(self):
        "Gera um Diário de Obra com gráfico de andamento por etapa"
        print(f"\n=== Diário de Obra — {self.nome_obra} ===")

        if not self.etapas:
            print("Nenhuma etapa cadastrada.")
            return

        nomes = []
        status_list = [] # Renomeado para não conflitar com variável 'status'
        cores = []
        concluidas = 0

        for etapa in self.etapas:
            nomes.append(etapa.titulo)
            status_list.append(etapa.status)
            if etapa.status == "Concluída":
                cores.append("green")
                concluidas += 1
            elif etapa.status == "Em andamento":
                cores.append("orange")
            else:
                cores.append("gray")

            # Exibição textual do DO
            resp = etapa.responsavel.nome if etapa.responsavel else "Não designado"
            print(f"\nEtapa: {etapa.titulo}")
            print(f"Descrição: {etapa.descricao}")
            print(f"Status: {etapa.status}")
            print(f"Responsável: {resp}")
            print(f"Data de entrega: {etapa.data_entrega}")

        # Geração do gráfico de andamento
        total = len(self.etapas)
        andamento = (concluidas / total) * 100 if total > 0 else 0

        try:
            plt.figure(figsize=(10, 6))
            # O gráfico de barras horizontal é melhor para listas de tarefas
            plt.barh(nomes, [1] * len(nomes), color=cores, align='center', height=0.5)
            plt.title(f"Andamento da Obra — {self.nome_obra}")
            plt.xlabel("Status")
            plt.ylabel("Etapas")
            # Remove os valores numéricos do eixo X, já que as cores são o indicador
            plt.xticks([])
            # Ajusta o layout para não cortar os nomes das etapas
            plt.tight_layout()

            # Salva o gráfico
            nome_arquivo = "diario_obra.png"
            plt.savefig(nome_arquivo)
            plt.show() # Mostra o gráfico no Colab

            print(f"\n[INFO] Diário de Obra gerado com sucesso!")
            print(f"Progresso geral da obra: {andamento:.1f}% concluído.")
            print(f"Gráfico salvo como '{nome_arquivo}'.")

        except Exception as e:
            print(f"\n[ERRO] Não foi possível gerar o gráfico: {e}")
            print("Verifique se a biblioteca matplotlib está instalada corretamente.")


    # --- Métodos de busca para o menu ---
    def buscar_funcionario_por_indice(self, indice_str):
        try:
            indice = int(indice_str) - 1
            if 0 <= indice < len(self.funcionarios):
                return self.funcionarios[indice]
        except: pass
        print("Índice de funcionário inválido.")
        return None

    def buscar_etapa_por_indice(self, indice_str):
        try:
            indice = int(indice_str) - 1
            if 0 <= indice < len(self.etapas):
                return self.etapas[indice]
        except: pass
        print("Índice de etapa inválido.")
        return None