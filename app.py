from flask import Flask

app = Flask("Ola")

@app.route("/")

def ola():
    return "Ola mundo,Bom dia"