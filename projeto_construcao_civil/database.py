import mysql.connector

# ------------------------------
# CONEXÃO
# ------------------------------

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Elias_0301!",
        database="construcao_civil", 
        ssl_disabled=True
    )


# ------------------------------
# INICIALIZAR BANCO
# ------------------------------

def inicializar_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS obras (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(150),
        data_criacao VARCHAR(20)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INT PRIMARY KEY,
        nome VARCHAR(150),
        funcao VARCHAR(100),
        telefone VARCHAR(20),
        data_contratacao VARCHAR(20),
        localizacao VARCHAR(100),
        obra_id INT,
        FOREIGN KEY (obra_id) REFERENCES obras(id) ON DELETE CASCADE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS etapas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        titulo VARCHAR(150),
        descricao TEXT,
        data_entrega VARCHAR(20),
        status VARCHAR(50),
        tipo_etapa VARCHAR(50),
        tipo_solo VARCHAR(100),
        material_principal VARCHAR(100),
        responsavel_id INT,
        obra_id INT,
        FOREIGN KEY (responsavel_id) REFERENCES funcionarios(id) ON DELETE SET NULL,
        FOREIGN KEY (obra_id) REFERENCES obras(id) ON DELETE CASCADE
    )
    """)

    conexao.commit()
    cursor.close()
    conexao.close()


# ------------------------------
# OBRA
# ------------------------------

def criar_obra(nome, data_criacao):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO obras (nome, data_criacao) VALUES (%s, %s)",
        (nome, data_criacao)
    )

    conexao.commit()
    obra_id = cursor.lastrowid

    cursor.close()
    conexao.close()
    return obra_id


# ------------------------------
# FUNCIONARIO
# ------------------------------

def inserir_funcionario(id_funcionario, nome, funcao, telefone,
                        data_contratacao, localizacao, obra_id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO funcionarios
        (id, nome, funcao, telefone, data_contratacao, localizacao, obra_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (id_funcionario, nome, funcao, telefone,
          data_contratacao, localizacao, obra_id))

    conexao.commit()
    cursor.close()
    conexao.close()
    return True


def atualizar_localizacao_funcionario(id_funcionario, nova_localizacao):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE funcionarios
        SET localizacao = %s
        WHERE id = %s
    """, (nova_localizacao, id_funcionario))

    conexao.commit()
    cursor.close()
    conexao.close()


def listar_funcionarios_por_obra(obra_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, funcao, localizacao
        FROM funcionarios
        WHERE obra_id = %s
    """, (obra_id,))

    dados = cursor.fetchall()

    cursor.close()
    conexao.close()
    return dados


def buscar_funcionario_por_id(id_funcionario):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, funcao, telefone, data_contratacao,
               localizacao, obra_id
        FROM funcionarios
        WHERE id = %s
    """, (id_funcionario,))

    dado = cursor.fetchone()

    cursor.close()
    conexao.close()
    return dado


# ------------------------------
# ETAPA
# ------------------------------

def inserir_etapa(titulo, descricao, data_entrega, status,
                  tipo_etapa, tipo_solo, material_principal,
                  responsavel_id, obra_id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO etapas
        (titulo, descricao, data_entrega, status,
         tipo_etapa, tipo_solo, material_principal,
         responsavel_id, obra_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (titulo, descricao, data_entrega, status,
          tipo_etapa, tipo_solo, material_principal,
          responsavel_id, obra_id))

    conexao.commit()
    etapa_id = cursor.lastrowid

    cursor.close()
    conexao.close()
    return etapa_id


def designar_responsavel_etapa(etapa_id, funcionario_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE etapas
        SET responsavel_id = %s
        WHERE id = %s
    """, (funcionario_id, etapa_id))

    conexao.commit()
    cursor.close()
    conexao.close()


def atualizar_status_etapa(etapa_id, novo_status):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE etapas
        SET status = %s
        WHERE id = %s
    """, (novo_status, etapa_id))

    conexao.commit()
    cursor.close()
    conexao.close()


def listar_etapas_por_obra(obra_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, titulo, descricao, data_entrega,
               status, tipo_etapa, tipo_solo,
               material_principal,
               (SELECT nome FROM funcionarios WHERE id = responsavel_id)
        FROM etapas
        WHERE obra_id = %s
    """, (obra_id,))

    dados = cursor.fetchall()

    cursor.close()
    conexao.close()
    return dados


def buscar_etapa_por_id(id_etapa):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, titulo, descricao, data_entrega,
               status, tipo_etapa, tipo_solo,
               material_principal, responsavel_id, obra_id
        FROM etapas
        WHERE id = %s
    """, (id_etapa,))

    dado = cursor.fetchone()

    cursor.close()
    conexao.close()
    return dado


# ------------------------------
# CONTAGENS E RELATÓRIOS
# ------------------------------

def contar_etapas_por_status(obra_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT COUNT(*) FROM etapas WHERE obra_id = %s
    """, (obra_id,))
    total = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*) FROM etapas
        WHERE obra_id = %s AND status = 'Concluída'
    """, (obra_id,))
    concluidas = cursor.fetchone()[0]

    cursor.close()
    conexao.close()

    return total, concluidas


def contar_etapas_funcionario(id_funcionario):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM etapas
        WHERE responsavel_id = %s
    """, (id_funcionario,))

    total = cursor.fetchone()[0]

    cursor.close()
    conexao.close()
    return total


def listar_etapas_por_funcionario(id_funcionario):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, titulo, descricao, data_entrega,
               status, tipo_etapa, tipo_solo,
               material_principal
        FROM etapas
        WHERE responsavel_id = %s
    """, (id_funcionario,))

    dados = cursor.fetchall()

    cursor.close()
    conexao.close()
    return dados


def listar_etapas_para_diario(obra_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT titulo, descricao, status,
               data_entrega, tipo_etapa,
               (SELECT nome FROM funcionarios WHERE id = responsavel_id)
        FROM etapas
        WHERE obra_id = %s
    """, (obra_id,))

    dados = cursor.fetchall()

    cursor.close()
    conexao.close()
    return dados
