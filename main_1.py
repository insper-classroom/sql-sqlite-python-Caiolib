import sqlite3

# Exercício de Python - Sqlite

# Conexão com o banco de dados dentro da pasta "db"
conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

# Vamos criar uma tabela chamada "Estudantes" com os seguintes campos:
# ID (chave primária) -  Criado automáticamente pela base de dados
# Nome
# Curso
# Ano de Ingresso

cursor.execute("""
CREATE TABLE IF NOT EXISTS Alunos (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    Ano_de_Ingresso INTEGER
);
""")

Alunos = [
        ('Ana Silva', 'Computação', '2019'),
        ('Pedro Mendes', 'Física', '2021'),
        ('Carla Souza', 'Computação', '2020'),
        ('João Alves', 'Matemática', '2018'),
        ('Maria Oliveira', 'Química', '2022')
]

cursor.executemany("""
INSERT INTO Alunos (Nome, Curso, Ano_de_Ingresso)
VALUES (?, ?, ?);
""", Alunos)

conn.commit()

cursor.execute("SELECT * FROM Alunos WHERE Ano_de_Ingresso BETWEEN 2019 AND 2020; ")

print(cursor.fetchall())

print('ATUALIZACAO')

cursor.execute("UPDATE Alunos SET Ano_de_Ingresso = 3000 WHERE ID = 1")
conn.commit()

cursor.execute("SELECT * FROM Alunos")
print(cursor.fetchall())


cursor.execute("DELETE FROM Alunos WHERE ID = 1")
conn.commit()
cursor.execute("SELECT * FROM Alunos")
print(cursor.fetchall())

cursor.execute("SELECT * FROM Alunos WHERE Curso = 'Computação' AND Ano_de_Ingresso > 2019")
conn.commit()

print(cursor.fetchall())

cursor.execute("UPDATE Alunos SET Ano_de_Ingresso = 2018 WHERE Curso = 'Computação'")
conn.commit()
cursor.execute("SELECT * FROM Alunos")
print(cursor.fetchall())