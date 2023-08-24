from db import db_utils as db # Importando o módulo db_utils.py do pacote db
import sqlite3

conn = sqlite3.connect('db/livros_database.db')
cursor = conn.cursor()

#Cria tabela
db.criar_tabela()

#adicionei um registro
db.inserir_registro('Caio', 'Computacao', 2000) 

#consulta um registro
db.consultar_registros()

#atualiza um registro
db.atualizar_registro(1, 2000)

#deleta um registro
db.deletar_registro(1)


cursor.execute("SELECT * FROM Alunos")
print(cursor.fetchall())

