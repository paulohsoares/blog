from flask import Flask

app = Flask("hello")

@app.route("/")
def hello():
    return "Hello World"

@app.route("/contato")
def hello():
    return "Paulo Henrique Soares. Estou Aqui"