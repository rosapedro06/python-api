from flask import Flask,request,jsonify
import sqlite3

app = Flask(__name__)

# Criando a conexão com o Banco
def db_conn():
    db = None
    try:
        db = sqlite3.connect('alunos.sqlite')
    except sqlite3.erro as e:
        print(e)
    return db

@app.route('/alunos',methods=['GET','POST'])
def alunos():
    db = db_conn()
    cursor = db.cursor()

    if request.method == 'GET':
        # Procura os alunos e volta eles em uma list
        data = cursor.execute("SELECT * FROM alunos").fetchall()
        print(data[0][1])
        return jsonify(list(data)), 200

    elif request.method == 'POST':
        # Cria um novo aluno
        data = request.get_json()
        cursor.execute("INSERT INTO alunos(nome,ano_escolar,nota) VALUES ('{0}',{1},{2})".format(data["nome"],data["ano_escolar"],data["nota"]))
        db.commit()

        return {"aluno" : data["nome"],"cadastrado?" : 400}, 200

@app.route('/alunos/<int:id>',methods=['GET','PUT','DELETE'])
def alunos_id(id):
    db = db_conn()
    cursor = db.cursor()

    if request.method == 'GET':
        # Seleciona só um aluno
        cursor.execute("SELECT * FROM alunos WHERE id={0}".format(id))
        aluno = cursor.fetchall()
        if aluno is not None:
            return jsonify(list(aluno)),200
        else:
            return "ID não encontrado", 404
    elif request.method == 'PUT':
        # Atualiza um aluno
        data = request.get_json()
        
        cursor.execute("UPDATE alunos SET nome='{0}', ano_escolar={1}, nota={2} WHERE id={3}".format(data["nome"],data["ano_escolar"],data["nota"],id))
        db.commit()

        return jsonify(data), 200
    elif request.method == 'DELETE':
        # Deleta um aluno
        cursor.execute("DELETE FROM alunos WHERE id={0}".format(id))
        db.commit()
        return {"deletado com sucesso?" : "sim"}, 200
        
if __name__ == "__main__":
    app.run()