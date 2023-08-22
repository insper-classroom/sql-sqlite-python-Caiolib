import sqlite3

# Função para criar uma tabela
def criar_tabela():
    conn = sqlite3.connect('db/livros_database.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Alunos (
        ID INTEGER PRIMARY KEY,
        Nome TEXT,
        Curso TEXT,
        "Ano de Ingresso" INTEGER
    )
    ''')

    conn.commit()
    conn.close()

# Função para inserir um novo registro
def inserir_registro(nome, curso, ano):
    conn = sqlite3.connect('db/livros_database.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO Alunos (Nome, Curso, "Ano de Ingresso")
    VALUES (?, ?, ?)
    ''', (nome, curso, ano))

    conn.commit()
    conn.close()

# Função para consultar registros
def consultar_registros():
    conn = sqlite3.connect('db/livros_database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Alunos')
    registros = cursor.fetchall()

    conn.close()
    return registros

# Função para atualizar um registro
def atualizar_registro(id, novo_ano):
    conn = sqlite3.connect('db/livros_database.db')
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE Alunos
    SET "Ano de Ingresso" = ?
    WHERE ID = ?
    ''', (novo_ano, id))

    conn.commit()
    conn.close()

# Função para deletar um registro
def deletar_registro(id):
    conn = sqlite3.connect('db/livros_database.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM Alunos WHERE ID = ?', (id,))

    conn.commit()
    conn.close()
