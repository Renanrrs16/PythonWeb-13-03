from flask import Flask, render_template, g
import sqlite3

app = Flask("Ola")

DATABASE = "banco.bd"
SECRET_KEY = "1234"

app.config.from_object(__name__)



def conectar():
    return sqlite3.connect(DATABASE)

def before_request():
    g.bd = conectar()

def teardown_request(f):
    g.bd.close()

@app.route("/")
def Ola():
    nomeUsuario = "Renan SOuza"
    listaUsuario = ["Renan", "Oseas", "Renata", "Rosi"]
    post = {"titulo": "Meu Titulo", "texto": "meu Texto", "data_criacao": "27/03/2024"}
    return render_template("hello.html", post = post)