from funcionario import Funcionario
from etapa import Etapa
from fundacao import EtapaFundacao, EtapaAcabamento
from IPython.display import clear_output
import matplotlib.pyplot as plt
import datetime 


#-----------------------------------------------------------------
# MENU PRINCIPAL (EXECUÇÃO)
# -----------------------------------------------------------------

def menu():
    """ Função principal que roda o menu interativo """

    # Pergunta o nome da obra ao iniciar
    nome_da_obra = input("Digite o nome da Obra para iniciar o sistema: ")
    if not nome_da_obra:
        nome_da_obra = "Obra Padrão" # Garante que não fique vazio

    obra = Obra(nome_da_obra)

    # --- DADOS INICIAIS REMOVIDOS ---

    # --- MENSAGEM DE BOAS-VINDAS E APRESENTAÇÃO ---
    clear_output(wait=True)
    print("================================================================")
    print(f"     Bem-vindo ao Sistema de Gerenciamento de Obras (SGO)")
    print("================================================================")
    print(f"\nObra atual: {obra.nome_obra}\n")
    print("Este sistema foi desenvolvido para centralizar o controle da sua construção.")
    print("Aqui você poderá:")
    print("  *  Cadastrar funcionários e gerenciar suas localizações.")
    print("  *  Criar e acompanhar o status de cada etapa do projeto.")
    print("  *  Gerar relatórios de progresso e diários de obra.")
    print("\n================================================================")

    input("\nPressione Enter para ir ao Menu Principal...") # Pausa inicial

    while True:
        clear_output(wait=True)

        print(f"\n--- Obra: {obra.nome_obra} ---")
        print("\n===== MENU PRINCIPAL =====")
        print("1. Adicionar Funcionário")
        print("2. Ver Detalhes de um Funcionário")
        print("3. Atualizar Localização de Funcionário")
        print("4. Cadastrar Nova Etapa")
        print("5. Designar Etapa a um Funcionário")
        print("6. Atualizar Status da Etapa")
        print("7. Listar Etapas por Funcionário")
        print("8. Listar Todos os Funcionários")
        print("9. Listar Todas as Etapas da Obra")
        print("10. Ver Relatório de Progresso")
        print("11. Gerar Diário de Obra (com Gráfico)") # <-- NOVA OPÇÃO
        print("===========================")
        print("0. Sair")
        opcao = input("\nEscolha uma opção (0-11): ") # <-- Menu atualizado

        if opcao == "1":
            print("\n--- Adicionar Novo Funcionário ---")
            id_func = input("ID do Funcionário (ex: 103): ")
            nome = input("Nome (ex: Joao Silva): ")
            funcao = input("Função (ex: Engenheiro, Pedreiro): ")
            tel = input("Telefone (ex: 7198888-7777): ")
            loc = input("Localização Inicial (ex: Almoxarifado, Bloco A): ")

            if not id_func or not nome or not funcao or not loc:
                print("\n[ERRO] ID, Nome, Função e Localização são obrigatórios.")
            else:
                novo_func = Funcionario(id_func, nome, funcao, tel, loc)
                obra.adicionar_funcionario(novo_func)

        elif opcao == "2":
            print("\n--- Ver Detalhes do Funcionário ---")
            if not obra.mostrar_funcionarios():
                input("Pressione Enter para continuar...")
                continue
            idx_f = input("Digite o número (da lista) do funcionário para ver os detalhes: ")
            func = obra.buscar_funcionario_por_indice(idx_f)
            if func:
                func.mostrar_info()

        elif opcao == "3":
            print("\n--- Atualizar Localização de Funcionário ---")
            if not obra.mostrar_funcionarios():
                input("Pressione Enter para continuar...")
                continue
            idx_f = input("Digite o número (da lista) do funcionário: ")
            func = obra.buscar_funcionario_por_indice(idx_f)
            if func:
                print(f"Localização atual de {func.nome}: {func.localizacao}")
                nova_loc = input("Digite a nova localização (ex: Bloco A, Andaime 3, Refeitório): ")
                if not nova_loc:
                    print("\n[ERRO] Localização não pode ser vazia.")
                else:
                    func.atualizar_localizacao(nova_loc)

        elif opcao == "4":
            print("--- Tipo da Etapa ---")
            print("1. Etapa de Fundação")
            print("2. Etapa de Acabamento")
            print("3. Etapa Padrão")

            while True:
                tipo = input("Escolha o tipo (1, 2 ou 3): ")
                if tipo in ["1", "2", "3"]: break
                print("[ERRO] Opção inválida. Digite 1, 2 ou 3.")

            titulo = input("Título da etapa (ex: Instalação Elétrica): ")
            desc = input("Descrição breve da etapa: ")
            data = input("Data de entrega (Formato: DD/MM/AAAA): ")

            if tipo == "1":
                solo = input("Tipo de solo (ex: Argiloso, Arenoso): ")
                nova_etapa = EtapaFundacao(titulo, desc, data, solo)
            elif tipo == "2":
                material = input("Material principal (ex: Tinta, Gesso): ")
                nova_etapa = EtapaAcabamento(titulo, desc, data, material)
            else:
                nova_etapa = Etapa(titulo, desc, data)
            obra.adicionar_etapa(nova_etapa)

        elif opcao == "5":
            if not obra.mostrar_etapas():
                input("Pressione Enter para continuar...")
                continue
            idx_e = input("Digite o índice da etapa: ")
            etapa = obra.buscar_etapa_por_indice(idx_e)

            if etapa:
                if not obra.mostrar_funcionarios():
                    input("Pressione Enter para continuar...")
                    continue
                idx_f = input("Digite o número do funcionário: ")
                func = obra.buscar_funcionario_por_indice(idx_f)
                if func:
                    etapa.designar_responsavel(func)

        elif opcao == "6":
            if not obra.mostrar_etapas():
                input("Pressione Enter para continuar...")
                continue
            idx_e = input("Digite o índice da etapa para atualizar: ")
            etapa = obra.buscar_etapa_por_indice(idx_e)

            if etapa:
                print(f"Status atual: {etapa.status}")
                status_validos = ["Pendente", "Em andamento", "Concluída"]
                while True:
                    novo = input("Novo status (Pendente / Em andamento / Concluída): ").strip().title()
                    if novo in status_validos:
                        etapa.atualizar_status(novo)
                        break
                    else:
                        print(f"[ERRO] Status inválido. Use um dos: {status_validos}")

        elif opcao == "7":
            if not obra.mostrar_funcionarios():
                input("Pressione Enter para continuar...")
                continue
            idx_f = input("Digite o número do funcionário para ver suas etapas: ")
            func = obra.buscar_funcionario_por_indice(idx_f)
            if func:
                func.listar_etapas_do_funcionario()

        elif opcao == "8":
            obra.mostrar_funcionarios()

        elif opcao == "9":
            obra.mostrar_etapas()

        elif opcao == "10":
            obra.gerar_relatorio_progresso()

        elif opcao == "11": # <-- NOVA OPÇÃO ADICIONADA
            obra.gerar_diario_obra()

        elif opcao == "0":
            print("Saindo do sistema...") # <-- MENSAGEM DE SAÍDA LIMPA
            break

        else:
            print("[ERRO] Opção inválida, tente novamente!")

        input("\nPressione Enter para continuar...")

# --- EXECUÇÃO DO PROGRAMA ---
menu()




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
