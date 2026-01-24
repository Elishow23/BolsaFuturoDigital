import sqlite3

# Nome do arquivo do banco de dados
DATABASE_NAME = 'obra.db'


@contextmanager
def get_db_connection():
    """Context manager para conexão com o banco de dados"""
    conn = sqlite3.connect(DATABASE_NAME)
    try:
        yield conn
    finally:
        conn.close()


def inicializar_banco():
    """Cria as tabelas do banco de dados se não existirem"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        
        # Tabela de Obras
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS obras (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                data_criacao TEXT
            )
        ''')
        
        # Tabela de Funcionários
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS funcionarios (
                id_funcionario TEXT PRIMARY KEY,
                nome TEXT NOT NULL,
                funcao TEXT NOT NULL,
                telefone TEXT,
                data_contratacao TEXT,
                localizacao TEXT NOT NULL,
                obra_id INTEGER,
                FOREIGN KEY (obra_id) REFERENCES obras(id)
            )
        ''')
        
        # Tabela de Etapas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS etapas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT,
                data_entrega TEXT,
                status TEXT DEFAULT 'Pendente',
                tipo_etapa TEXT DEFAULT 'Padrao',
                tipo_solo TEXT,
                material_principal TEXT,
                responsavel_id TEXT,
                obra_id INTEGER,
                FOREIGN KEY (responsavel_id) REFERENCES funcionarios(id_funcionario),
                FOREIGN KEY (obra_id) REFERENCES obras(id)
            )
        ''')
        
        conn.commit()
        print("[INFO] Banco de dados inicializado com sucesso!")


# =================================================================
# FUNÇÕES CRUD PARA OBRAS
# =================================================================

def criar_obra(nome, data_criacao):
    """Cria uma nova obra no banco de dados"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO obras (nome, data_criacao) VALUES (?, ?)
        ''', (nome, data_criacao))
        conn.commit()
        return cursor.lastrowid


def buscar_obra_por_id(obra_id):
    """Busca uma obra pelo ID"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, nome, data_criacao FROM obras WHERE id = ?', (obra_id,))
        return cursor.fetchone()


# =================================================================
# FUNÇÕES CRUD PARA FUNCIONÁRIOS
# =================================================================

def inserir_funcionario(id_funcionario, nome, funcao, telefone, data_contratacao, localizacao, obra_id):
    """Insere um novo funcionário no banco de dados"""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO funcionarios (id_funcionario, nome, funcao, telefone, 
                                         data_contratacao, localizacao, obra_id)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (id_funcionario, nome, funcao, telefone, data_contratacao, localizacao, obra_id))
            conn.commit()
            return True
    except sqlite3.IntegrityError:
        print(f"[ERRO] Funcionário com ID {id_funcionario} já existe.")
        return False


def atualizar_localizacao_funcionario(id_funcionario, nova_localizacao):
    """Atualiza a localização de um funcionário"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE funcionarios SET localizacao = ? WHERE id_funcionario = ?
        ''', (nova_localizacao, id_funcionario))
        conn.commit()


def buscar_funcionario_por_id(id_funcionario):
    """Busca um funcionário pelo ID"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id_funcionario, nome, funcao, telefone, data_contratacao, localizacao, obra_id
            FROM funcionarios WHERE id_funcionario = ?
        ''', (id_funcionario,))
        return cursor.fetchone()


def listar_funcionarios_por_obra(obra_id):
    """Lista todos os funcionários de uma obra"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id_funcionario, nome, funcao, localizacao 
            FROM funcionarios WHERE obra_id = ?
            ORDER BY nome
        ''', (obra_id,))
        return cursor.fetchall()


def contar_etapas_funcionario(id_funcionario):
    """Conta quantas etapas um funcionário possui"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT COUNT(*) FROM etapas WHERE responsavel_id = ?
        ''', (id_funcionario,))
        return cursor.fetchone()[0]


# =================================================================
# FUNÇÕES CRUD PARA ETAPAS
# =================================================================

def inserir_etapa(titulo, descricao, data_entrega, status, tipo_etapa, tipo_solo, material_principal, responsavel_id, obra_id):
    """Insere uma nova etapa no banco de dados"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO etapas (titulo, descricao, data_entrega, status, tipo_etapa,
                               tipo_solo, material_principal, responsavel_id, obra_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (titulo, descricao, data_entrega, status, tipo_etapa, tipo_solo, material_principal, responsavel_id, obra_id))
        conn.commit()
        return cursor.lastrowid


def atualizar_status_etapa(etapa_id, novo_status):
    """Atualiza o status de uma etapa"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE etapas SET status = ? WHERE id = ?
        ''', (novo_status, etapa_id))
        conn.commit()


def designar_responsavel_etapa(etapa_id, id_funcionario):
    """Designa um funcionário como responsável por uma etapa"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE etapas SET responsavel_id = ? WHERE id = ?
        ''', (id_funcionario, etapa_id))
        conn.commit()


def listar_etapas_por_obra(obra_id):
    """Lista todas as etapas de uma obra com informações do responsável"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT e.id, e.titulo, e.descricao, e.data_entrega, e.status, 
                   e.tipo_etapa, e.tipo_solo, e.material_principal,
                   f.nome as responsavel_nome
            FROM etapas e
            LEFT JOIN funcionarios f ON e.responsavel_id = f.id_funcionario
            WHERE e.obra_id = ?
            ORDER BY e.id
        ''', (obra_id,))
        return cursor.fetchall()


def listar_etapas_por_funcionario(id_funcionario):
    """Lista todas as etapas de um funcionário específico"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, titulo, descricao, data_entrega, status, tipo_etapa, 
                   tipo_solo, material_principal
            FROM etapas WHERE responsavel_id = ?
            ORDER BY id
        ''', (id_funcionario,))
        return cursor.fetchall()


def buscar_etapa_por_id(etapa_id):
    """Busca uma etapa pelo ID"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, titulo, descricao, data_entrega, status, tipo_etapa,
                   tipo_solo, material_principal, responsavel_id, obra_id
            FROM etapas WHERE id = ?
        ''', (etapa_id,))
        return cursor.fetchone()


# =================================================================
# FUNÇÕES DE RELATÓRIO
# =================================================================

def contar_etapas_por_status(obra_id):
    """Conta etapas por status para relatório de progresso"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM etapas WHERE obra_id = ?', (obra_id,))
        total = cursor.fetchone()[0]
        
        cursor.execute('''
            SELECT COUNT(*) FROM etapas WHERE obra_id = ? AND status = 'Concluída'
        ''', (obra_id,))
        concluidas = cursor.fetchone()[0]
        
        return total, concluidas


def listar_etapas_para_diario(obra_id):
    """Lista etapas formatadas para o diário de obra"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT e.titulo, e.descricao, e.status, e.data_entrega, e.tipo_etapa,
                   f.nome as responsavel_nome
            FROM etapas e
            LEFT JOIN funcionarios f ON e.responsavel_id = f.id_funcionario
            WHERE e.obra_id = ?
            ORDER BY e.id
        ''', (obra_id,))
        return cursor.fetchall()
