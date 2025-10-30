from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def principal():
    return jsonify({"message", "Bem vindo ao Flask"})

@app.route('/sobre')
def sobre():
    return "<h1> Bem-vindo ao Python"