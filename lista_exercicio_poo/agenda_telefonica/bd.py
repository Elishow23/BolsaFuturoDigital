import pymysql

class AddressBook:
    def __init__(self):
        # Configuração centralizada do banco
        self.config = {
            'host': '127.0.0.1',
            'user': 'root',
            'password': 'Elias_0301!',
            'database': 'agenda_telefonica',
            'cursorclass': pymysql.cursors.DictCursor
        }

    def _conectar(self):
        """Método auxiliar para abrir conexão"""
        return pymysql.connect(**self.config)

    def add_contact(self, id, nome, telefone, email):
        conexao = None
        try:
            conexao = self._conectar()
            with conexao.cursor() as cursor:
                # Primeiro, verificamos o limite de 10 contatos que você tinha no original
                cursor.execute("SELECT COUNT(*) as total FROM contatos")
                total = cursor.fetchone()['total']

                if total < 10:
                    sql = "INSERT INTO contatos (id, nome, telefone, email) VALUES (%s, %s, %s, %s)"
                    cursor.execute(sql, (id, nome, telefone, email))
                    conexao.commit()
                    print(f'Contato {nome} adicionado com sucesso!')
                else:
                    print('Ops, você já tem mais de 10 contatos no banco!')
        except Exception as e:
            print(f"Erro ao adicionar: {e}")
        finally:
            if conexao: conexao.close()

    def list_contacts(self):
        conexao = None
        try:
            conexao = self._conectar()
            with conexao.cursor() as cursor:
                cursor.execute("SELECT * FROM contatos")
                contatos = cursor.fetchall()
                
                if not contatos:
                    print("A agenda está vazia!")
                    return
                
                print("\n--- LISTA DE CONTATOS ---")
                for c in contatos:
                    print(f"{c['id']} - Nome: {c['nome']} | Tel: {c['telefone']} | Email: {c['email']}")
        finally:
            if conexao: conexao.close()

    def update_contact(self, id, nome, telefone, email):
        conexao = None
        try:
            conexao = self._conectar()
            with conexao.cursor() as cursor:
                sql = "UPDATE contatos SET nome=%s, telefone=%s, email=%s WHERE id=%s"
                cursor.execute(sql, (nome, telefone, email, id))
                conexao.commit()
                
                if cursor.rowcount > 0:
                    print(f'Usuário {nome} atualizado com sucesso!')
                else:
                    print(f"ID {id} não encontrado.")
        finally:
            if conexao: conexao.close()

    def pesquisar(self, nome):
        conexao = None
        try:
            conexao = self._conectar()
            with conexao.cursor() as cursor:
                # Usamos LIKE para encontrar nomes parecidos (ex: 'Eli' acha 'Eliseu')
                sql = "SELECT * FROM contatos WHERE nome LIKE %s"
                cursor.execute(sql, (f"%{nome}%",))
                resultados = cursor.fetchall()
                
                if not resultados:
                    print('Contato não encontrado')
                    return
                
                for r in resultados:
                    print(f"{r['id']} - Nome: {r['nome']} | Tel: {r['telefone']} | Email: {r['email']}")
        finally:
            if conexao: conexao.close()

    def deletar(self, id):
        conexao = None
        try:
            conexao = self._conectar()
            with conexao.cursor() as cursor:
                sql = "DELETE FROM contatos WHERE id=%s"
                cursor.execute(sql, (id,))
                conexao.commit()
                
                if cursor.rowcount > 0:
                    print(f"Contato com ID {id} excluído com sucesso!")
                else:
                    print(f"Erro: ID {id} não encontrado.")
        finally:
            if conexao: conexao.close()