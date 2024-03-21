from flask import Flask, render_template

app = Flask("Ola")

@app.route("/")
@app.route("/teste")
def ola():
    return "Ola mundo,Bom dia"

@app.route("/alunos")
def alunos():
    return render_template("hello.html")