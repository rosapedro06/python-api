import sqlite3

db = sqlite3.connect("alunos.sqlite")

# Table

cursor = db.cursor()

cursor.execute("CREATE TABLE alunos ( id integer primary key autoincrement,nome text,ano_escolar intenger, nota intenger)")


# Dados artificiais

#cursor.execute("INSERT INTO alunos(nome,ano_escolar,nota) VALUES('Pedro',9,80)")
#cursor.execute("INSERT INTO alunos(nome,ano_escolar,nota) VALUES('Maria',2,90)")
#cursor.execute("INSERT INTO alunos(nome,ano_escolar,nota) VALUES('Julia',9,60)")
#cursor.execute("INSERT INTO alunos(nome,ano_escolar,nota) VALUES('Gabriel',8,90)")
#cursor.execute("INSERT INTO alunos(nome,ano_escolar,nota) VALUES('Joao',6,20)")
#db.commit()