from flask import Flask, render_template


app = Flask("hello")

@app.route("/")
def hello():
    return render_template("index.html", nome=nomeAula)

@app.route("/contato")
def contato():
    nomeAula = "Aula python para Web"
    return render_template("contatos.html", nome=nomeAula)

@app.route("/usuario")
def usuario():
    usuario = [1,"Paulo Henrique Soares", "Aluno"]
    alunos = ["Andre Guedes","Paulo Henrique Soares", "Raiane Caroline", "Alicia Duarte"]
    return render_template("usuario.html", user=usuario, alunos=alunos)

    