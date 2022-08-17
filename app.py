from flask import Flask, render_template
from datetime import datetime

app = Flask("hello")

posts = [
    {"title": "Meu primeiro post", "body": "Esse post é o primeiro blog", "author": "Paulo Soares", "created": datetime(2022,8,17)},
    {"title": "Meu segundo post", "body": "Esse post é o segundo blog", "author": "Paulo Henrique", "created": datetime(2022,8,17)},
    {"title": "Meu terceiro post", "body": "Esse post é o terceiro blog", "author": "Henrique Soares", "created": datetime(2022,8,17)}
]

@app.route("/")
def index():
    return render_template("index.html", posts=posts)
