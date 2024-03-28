from flask import Flask, render_template, g
import sqlite3

app = Flask("Ola")

DATABASE = "banco.bd"
SECRET_KEY = "1234"

app.config.from_object(__name__)



def conectar():
    return sqlite3.connect(DATABASE)

@app.before_request
def before_request():
    g.bd = conectar()

@app.teardown_request
def teardown_request(f):
    g.bd.close()

@app.route("/")
def exibir_posts():
    sql = "SELECT titulo, texto, data_criacao FROM posts ORDER BY id DESC"
    resultado = g.bd.execute(sql)
    post = []

    for titulo, texto, data_criacao in resultado.fetchall():
        post.append({
            "titulo":titulo,
            "texto":texto,
            "data_criacao":data_criacao
        })
    return render_template("exibir_posts.html", post = post)