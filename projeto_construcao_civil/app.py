from IPython.display import clear_output
import database as db
from models import Obra, Funcionario, Etapa, EtapaFundacao, EtapaAcabamento


# -----------------------------------------------------------------
# MENU PRINCIPAL (EXECUÇÃO)
# -----------------------------------------------------------------

def menu():
    """Função principal que roda o menu interativo"""
    
    # Inicializa o banco de dados
    db.inicializar_banco()

    # Pergunta o nome da obra ao iniciar
    nome_da_obra = input("Digite o nome da Obra para iniciar o sistema: ")
    if not nome_da_obra:
        nome_da_obra = "Obra Padrão"

    obra = Obra(nome_da_obra)

    # Mensagem de boas-vindas
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

    input("\nPressione Enter para ir ao Menu Principal...")

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
        print("11. Gerar Diário de Obra (com Gráfico)")
        print("===========================")
        print("0. Sair")
        opcao = input("\nEscolha uma opção (0-11): ")

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
                novo_func = Funcionario(id_func, nome, funcao, tel, loc, obra.id)
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
                nova_etapa = EtapaFundacao(titulo, desc, data, solo, obra.id)
            elif tipo == "2":
                material = input("Material principal (ex: Tinta, Gesso): ")
                nova_etapa = EtapaAcabamento(titulo, desc, data, material, obra.id)
            else:
                nova_etapa = Etapa(titulo, desc, data, obra.id)
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

        elif opcao == "11":
            obra.gerar_diario_obra()

        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("[ERRO] Opção inválida, tente novamente!")

        input("\nPressione Enter para continuar...")


# --- EXECUÇÃO DO PROGRAMA ---
if __name__ == "__main__":
    menu()
