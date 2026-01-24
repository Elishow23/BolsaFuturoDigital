import datetime
import database as db


# -----------------------------------------------------------------
# CLASSE FUNCIONARIO
# -----------------------------------------------------------------

class Funcionario:
    """Representa um funcionário da obra"""
    
    def __init__(self, id_funcionario, nome, funcao, telefone, localizacao_inicial, obra_id):
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.funcao = funcao
        self.telefone = telefone
        self.data_contratacao = datetime.date.today().strftime('%d/%m/%Y')
        self.localizacao = localizacao_inicial
        self.obra_id = obra_id

    def salvar(self):
        """Salva o funcionário no banco de dados"""
        return db.inserir_funcionario(
            self.id_funcionario, 
            self.nome, 
            self.funcao, 
            self.telefone,
            self.data_contratacao, 
            self.localizacao, 
            self.obra_id
        )

    def atualizar_localizacao(self, nova_localizacao):
        """Atualiza a localização do funcionário"""
        self.localizacao = nova_localizacao
        db.atualizar_localizacao_funcionario(self.id_funcionario, nova_localizacao)
        print(f"Localização de {self.nome} atualizada para: {self.localizacao}")

    def mostrar_info(self):
        """Mostra os dados detalhados do funcionário"""
        print(f"\n--- Detalhes do Funcionário ID: {self.id_funcionario} ---")
        print(f"Nome: {self.nome}")
        print(f"Função: {self.funcao}")
        print(f"Telefone: {self.telefone}")
        print(f"Data de Contratação: {self.data_contratacao}")
        print(f"Localização Atual: {self.localizacao}")
        
        total_etapas = db.contar_etapas_funcionario(self.id_funcionario)
        print(f"Total de Etapas Designadas: {total_etapas}")

    def listar_etapas_do_funcionario(self):
        """Lista todas as etapas do funcionário"""
        print(f"\n--- Etapas de {self.nome} (ID: {self.id_funcionario}) ---")
        
        etapas = db.listar_etapas_por_funcionario(self.id_funcionario)
        
        if not etapas:
            print("Nenhuma etapa designada.")
        else:
            for etapa in etapas:
                id_etapa, titulo, desc, data, status, tipo, solo, material = etapa
                
                if tipo == 'Fundacao':
                    print(f"\n  [ETAPA FUNDAÇÃO] {titulo} ({status})")
                    print(f"    Tipo de Solo: {solo} | Responsável: {self.nome}")
                    print(f"    Entrega: {data} | Descrição: {desc}")
                elif tipo == 'Acabamento':
                    print(f"\n  [ETAPA ACABAMENTO] {titulo} ({status})")
                    print(f"    Material: {material} | Responsável: {self.nome}")
                    print(f"    Entrega: {data} | Descrição: {desc}")
                else:
                    print(f"  [Etapa Padrão] {titulo} ({status})")
                    print(f"    Descrição: {desc}")
                    print(f"    Responsável: {self.nome} | Entrega: {data}")


# -----------------------------------------------------------------
# CLASSE ETAPA (BASE)
# -----------------------------------------------------------------

class Etapa:
    """Classe base para uma Etapa da Obra"""
    
    def __init__(self, titulo, descricao, data_entrega, obra_id, tipo_etapa='Padrao'):
        self.id = None
        self.titulo = titulo
        self.descricao = descricao
        self.data_entrega = data_entrega
        self.status = "Pendente"
        self.responsavel = None
        self.obra_id = obra_id
        self.tipo_etapa = tipo_etapa
        self.tipo_solo = None
        self.material_principal = None

    def salvar(self):
        """Salva a etapa no banco de dados"""
        self.id = db.inserir_etapa(
            self.titulo,
            self.descricao,
            self.data_entrega,
            self.status,
            self.tipo_etapa,
            self.tipo_solo,
            self.material_principal,
            self.responsavel.id_funcionario if self.responsavel else None,
            self.obra_id
        )

    def designar_responsavel(self, funcionario):
        """Designa um funcionário como responsável"""
        if isinstance(funcionario, Funcionario):
            self.responsavel = funcionario
            db.designar_responsavel_etapa(self.id, funcionario.id_funcionario)
            print(f"Etapa '{self.titulo}' designada para {funcionario.nome}.")
        else:
            print("Erro: Só é possível designar para um Funcionario.")

    def atualizar_status(self, novo_status):
        """Atualiza o status da etapa"""
        if novo_status in ["Pendente", "Em andamento", "Concluída"]:
            self.status = novo_status
            db.atualizar_status_etapa(self.id, novo_status)
            print(f"Status da etapa '{self.titulo}' alterado para '{novo_status}'.")
        else:
            print(f"Erro: Status '{novo_status}' é inválido.")

    def exibir_detalhes(self):
        """Método base para Polimorfismo"""
        resp = self.responsavel.nome if self.responsavel else "Ninguém"
        print(f"  [Etapa Padrão] {self.titulo} ({self.status})")
        print(f"    Descrição: {self.descricao}")
        print(f"    Responsável: {resp} | Entrega: {self.data_entrega}")


# -----------------------------------------------------------------
# CLASSE ETAPA FUNDAÇÃO (HERANÇA)
# -----------------------------------------------------------------

class EtapaFundacao(Etapa):
    """Classe filha para etapas de fundação"""
    
    def __init__(self, titulo, descricao, data_entrega, tipo_solo, obra_id):
        super().__init__(titulo, descricao, data_entrega, obra_id, 'Fundacao')
        self.tipo_solo = tipo_solo

    def exibir_detalhes(self):
        """POLIMORFISMO: sobrescreve o método da classe-pai"""
        resp = self.responsavel.nome if self.responsavel else "Ninguém"
        print(f"\n  [ETAPA FUNDAÇÃO] {self.titulo} ({self.status})")
        print(f"    Tipo de Solo: {self.tipo_solo} | Responsável: {resp}")
        print(f"    Entrega: {self.data_entrega} | Descrição: {self.descricao}")


# -----------------------------------------------------------------
# CLASSE ETAPA ACABAMENTO (HERANÇA)
# -----------------------------------------------------------------

class EtapaAcabamento(Etapa):
    """Classe filha para etapas de acabamento"""
    
    def __init__(self, titulo, descricao, data_entrega, material_principal, obra_id):
        super().__init__(titulo, descricao, data_entrega, obra_id, 'Acabamento')
        self.material_principal = material_principal

    def exibir_detalhes(self):
        """POLIMORFISMO: outra implementação do método"""
        resp = self.responsavel.nome if self.responsavel else "Ninguém"
        print(f"\n  [ETAPA ACABAMENTO] {self.titulo} ({self.status})")
        print(f"    Material: {self.material_principal} | Responsável: {resp}")
        print(f"    Entrega: {self.data_entrega} | Descrição: {self.descricao}")


# -----------------------------------------------------------------
# CLASSE OBRA (GERENCIADORA)
# -----------------------------------------------------------------

class Obra:
    """Gerencia a obra, funcionários e etapas"""
    
    def __init__(self, nome_obra):
        self.nome_obra = nome_obra
        self.id = None
        self._criar_obra()

    def _criar_obra(self):
        """Cria a obra no banco de dados"""
        data_criacao = datetime.date.today().strftime('%d/%m/%Y')
        self.id = db.criar_obra(self.nome_obra, data_criacao)

    def adicionar_funcionario(self, funcionario):
        """Adiciona um novo funcionário à obra"""
        if funcionario.salvar():
            print(f"Funcionário {funcionario.nome} (ID: {funcionario.id_funcionario}) adicionado à obra.")

    def adicionar_etapa(self, etapa):
        """Adiciona uma nova etapa ao projeto"""
        etapa.salvar()
        print(f"Etapa '{etapa.titulo}' adicionada à obra.")

    def mostrar_funcionarios(self):
        """Lista todos os funcionários"""
        print(f"\n--- Funcionários da Obra {self.nome_obra} ---")
        funcionarios = db.listar_funcionarios_por_obra(self.id)
        
        if not funcionarios:
            print("Nenhum funcionário cadastrado.")
            return False

        for i, (id_func, nome, funcao, loc) in enumerate(funcionarios):
            print(f"  {i+1}. ID: {id_func} | {nome} ({funcao}) | Local: {loc}")
        return True

    def mostrar_etapas(self):
        """Lista todas as etapas"""
        print(f"\n--- Etapas da Obra {self.nome_obra} ---")
        etapas = db.listar_etapas_por_obra(self.id)
        
        if not etapas:
            print("Nenhuma etapa cadastrada.")
            return False

        for i, etapa in enumerate(etapas):
            id_e, titulo, desc, data, status, tipo, solo, material, resp = etapa
            resp = resp if resp else "Ninguém"
            print(f"\n  (Índice {i+1})")
            
            if tipo == 'Fundacao':
                print(f"  [ETAPA FUNDAÇÃO] {titulo} ({status})")
                print(f"    Tipo de Solo: {solo} | Responsável: {resp}")
                print(f"    Entrega: {data} | Descrição: {desc}")
            elif tipo == 'Acabamento':
                print(f"  [ETAPA ACABAMENTO] {titulo} ({status})")
                print(f"    Material: {material} | Responsável: {resp}")
                print(f"    Entrega: {data} | Descrição: {desc}")
            else:
                print(f"  [Etapa Padrão] {titulo} ({status})")
                print(f"    Descrição: {desc}")
                print(f"    Responsável: {resp} | Entrega: {data}")
        return True

    def gerar_relatorio_progresso(self):
        """Relatório de Progresso"""
        print(f"\n--- Relatório de Progresso: {self.nome_obra} ---")
        
        total, concluidas = db.contar_etapas_por_status(self.id)
        
        if total == 0:
            print("Nenhuma etapa cadastrada.")
            return

        pendentes_andamento = total - concluidas
        print(f"Total de Etapas: {total}")
        print(f"Etapas Concluídas: {concluidas}")
        print(f"Etapas Pendentes/Em Andamento: {pendentes_andamento}")
        print("---------------------------------")

    def gerar_diario_obra(self):
        """Gera um Diário de Obra com gráfico de andamento"""
        import matplotlib.pyplot as plt
        
        print(f"\n=== Diário de Obra — {self.nome_obra} ===")
        
        etapas = db.listar_etapas_para_diario(self.id)

        if not etapas:
            print("Nenhuma etapa cadastrada.")
            return

        nomes = []
        cores = []
        concluidas = 0

        for etapa in etapas:
            titulo, desc, status, data, tipo, resp = etapa
            nomes.append(titulo)
            
            if status == "Concluída":
                cores.append("green")
                concluidas += 1
            elif status == "Em andamento":
                cores.append("orange")
            else:
                cores.append("gray")

            # Exibição textual
            resp = resp if resp else "Não designado"
            print(f"\nEtapa: {titulo}")
            print(f"Descrição: {desc}")
            print(f"Status: {status}")
            print(f"Responsável: {resp}")
            print(f"Data de entrega: {data}")

        # Gráfico
        total = len(etapas)
        andamento = (concluidas / total) * 100 if total > 0 else 0

        try:
            plt.figure(figsize=(10, 6))
            plt.barh(nomes, [1] * len(nomes), color=cores, align='center', height=0.5)
            plt.title(f"Andamento da Obra — {self.nome_obra}")
            plt.xlabel("Status")
            plt.ylabel("Etapas")
            plt.xticks([])
            plt.tight_layout()

            nome_arquivo = "diario_obra.png"
            plt.savefig(nome_arquivo)
            plt.show()

            print(f"\n[INFO] Diário de Obra gerado com sucesso!")
            print(f"Progresso geral da obra: {andamento:.1f}% concluído.")
            print(f"Gráfico salvo como '{nome_arquivo}'.")

        except Exception as e:
            print(f"\n[ERRO] Não foi possível gerar o gráfico: {e}")

    def buscar_funcionario_por_indice(self, indice_str):
        """Busca funcionário por índice da lista"""
        try:
            indice = int(indice_str) - 1
            funcionarios = db.listar_funcionarios_por_obra(self.id)
            
            if 0 <= indice < len(funcionarios):
                func_data = funcionarios[indice]
                # Busca dados completos
                func_completo = db.buscar_funcionario_por_id(func_data[0])
                if func_completo:
                    id_f, nome, funcao, tel, data_cont, loc, obra_id = func_completo
                    func = Funcionario(id_f, nome, funcao, tel, loc, obra_id)
                    func.data_contratacao = data_cont
                    return func
        except:
            pass
        print("Índice de funcionário inválido.")
        return None

    def buscar_etapa_por_indice(self, indice_str):
        """Busca etapa por índice da lista"""
        try:
            indice = int(indice_str) - 1
            etapas = db.listar_etapas_por_obra(self.id)
            
            if 0 <= indice < len(etapas):
                etapa_data = etapas[indice]
                id_e = etapa_data[0]
                
                # Busca dados completos da etapa
                etapa_completa = db.buscar_etapa_por_id(id_e)
                if etapa_completa:
                    id_e, titulo, desc, data, status, tipo, solo, material, resp_id, obra_id = etapa_completa
                    
                    if tipo == 'Fundacao':
                        etapa = EtapaFundacao(titulo, desc, data, solo, obra_id)
                    elif tipo == 'Acabamento':
                        etapa = EtapaAcabamento(titulo, desc, data, material, obra_id)
                    else:
                        etapa = Etapa(titulo, desc, data, obra_id)
                    
                    etapa.id = id_e
                    etapa.status = status
                    
                    # Buscar responsável se existir
                    if resp_id:
                        func_data = db.buscar_funcionario_por_id(resp_id)
                        if func_data:
                            id_f, nome, funcao, tel, data_cont, loc, obra_id = func_data
                            etapa.responsavel = Funcionario(id_f, nome, funcao, tel, loc, obra_id)
                            etapa.responsavel.data_contratacao = data_cont
                    
                    return etapa
        except Exception as e:
            print(f"Erro ao buscar etapa: {e}")
        print("Índice de etapa inválido.")
        return None
