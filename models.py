import sqlite3

class PessoaCRUD:

    def __init__(self, db_name = 'pessoas.db'):
        self.db_name = db_name
    # _ no começo porque é um metodo privado, ou seja, principalmente dentro desta classe
    def _connect(self):
        """conectar ao bonco de dados e retornar a conexão"""
        conexao = sqlite3.connect(self.db_name)
        #cursor == 'objeto que permite executar comandos sql e recuperar dados'
        cursor = conexao.cursor()
        return conexao, cursor

    def create(self, nome, idade ):
        """Inserir uma nova pessoa no banco de dados"""
        conexao, cursor = self._connect()
        cursor.execute('INSERT INTO pessoa(nome, idade) VALUES (?, ?)', (nome, idade))
        conexao.commit()
        conexao.close()

    def read(self, id=None):
        """Ler e retornar informações de uma ou todas as pessoas."""
        conexao, cursor = self._connect()
        if id:
            cursor.execute('SELECT * FROM pessoa WHERE id=?', (id,))
            pessoa = cursor.fetchone()
        else:
            cursor.execute('SELECT * FROM pessoa')
            pessoa = cursor.fetchall()
        conexao.close()
        return pessoa

    def update(self, id, novo_nome, nova_idade):
        """Atualizar informações de uma pessoa com um ID específico."""
        conexao, cursor = self._connect()
        cursor.execute('UPDATE pessoa SET nome=?, idade=? WHERE id=?', (novo_nome, nova_idade, id))
        conexao.commit()
        conexao.close()

    def delete(self, id):
        """Deletar uma pessoa com um ID específico."""
        conexao, cursor = self._connect()
        cursor.execute('DELETE FROM pessoa WHERE id=?', (id,))
        conexao.commit()
        conexao.close()