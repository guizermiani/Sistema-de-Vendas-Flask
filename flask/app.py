from flask import Flask, render_template, request
from conexao import conecta_db
from categoria import inserir

app = Flask(__name__)

@app.route('/')
def principal():
    nome = "Guilherme Zermiani"
    return render_template("index.html", nome=nome)


@app.route("/listar-categoria", methods=["GET"])
def listar_categoria():
    cursor = conecta_db().cursor()
    cursor.execute("SELECT id, nome FROM categoria")
    registros = cursor.fetchall()
    
    resultado = "<h2>Registros da tabela categoria:</h2><ul>"
    for registro in registros:
        resultado += f"<li>ID: {registro[0]}, Nome: {registro[1]}</li>"
    resultado += "</ul>"
    
    return render_template("categoria-list.html", categorias=registros)




@app.route("/salvar-categoria", methods=["GET", "POST"])
def salvar_categoria():
    conexao = conecta_db()
    if request.method == "POST":
        nome = request.form['nome']
        if not nome:
            return "<h3>Por favor, preencha o nome da categoria.</h3>"
        
        conexao = conecta_db()
        inserir(conexao,nome)
        
        return f"<h2>Categoria "{nome}"" salva com sucesso!</h2>"
    return render_template("categoria-form.html")

if __name__ == '__main__':
    app.run(debug=True)