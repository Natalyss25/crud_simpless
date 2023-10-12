import sqlite3


def database():
    # Conectar (ou criar, se não existir) ao banco de dados 'pessoas.db'
    conexao = sqlite3.connect('pessoas.db')
    cursor = conexao.cursor()

    # Criar a tabela 'pessoa', caso ela não exista
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoa (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL
    )
    ''')

    conexao.commit()
    conexao.close()


if __name__ == "__main__":
    database()
