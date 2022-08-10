from flask import Flask

app = Flask("hello")

@app.route("/")
def hello():
    return "Hello World"

@app.route("/contato")
def contato():
    return """
    <html>
        <head>
            <title>Contatos</title>
        </head>
        <body>
            <div style='border: 2px solid red; padding: 10px; border-radius: 8px; background-color: teal;text-align: center;'>
                <h1>Paulo Henrique Soares. Estou Aqui</h1>
            </div>
        </body>
    </html>
    """
    