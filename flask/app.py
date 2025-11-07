from flask import Flask, render_template, request
from conexao import conecta_db
from categoria_bd import inserir_categoria
from cliente_bd import inserir_cliente, listar_clientes_bd

app = Flask(__name__)

@app.route('/')
def principal():
    nome = "Guilherme Zermiani"
    return render_template("index.html", nome=nome)

@app.route('/cliente', methods=['GET', 'POST'])
def salvar_cliente():
     if request.method == 'POST':
        nome = request.form.get('nome')
        celular = request.form.get('celular')
        email = request.form.get('email')
        cpf_cnpj = request.form.get('cpf_cnpj')
        
        if not nome:
            return "<h3> Por favor, preencha todos os campos</h3"
        
        conexao = conecta_db()
        inserir_cliente(conexao,nome, celular, email, cpf_cnpj)

        return f"<h2> Cliente Salvo com Sucesso:  {nome} </h2>"
     return render_template("cliente-form.html")
 
@app.route("/listar-clientes", methods=["GET"])
def listar_clientes():
    conexao = conecta_db()
    clientes = listar_clientes_bd(conexao)
    return render_template("cliente-listar.html", clientes=clientes)

@app.route("/salvar-categoria", methods=['GET','POST'])
def salvar_categoria():
    if request.method == 'POST':
        nome = request.form.get('nome')
        if not nome:
            return "<h3> Por favor, preencha todos os campos</h3"
        
        conexao = conecta_db()
        inserir_categoria(conexao,nome)

        return f"<h2> Categoria Salva com Sucesso:  {nome} </h2>"
    return render_template("categoria-form.html")


@app.route("/deletar-categoria", methods=["POST", "GET"])
def deletar_categoria():
    if request.method == "POST":
        id_categoria = request.form['id']
        
        conexao = conecta_db()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM categoria WHERE id = %s", (id_categoria,))
        
        conexao.commit()
        
        return "Categoria excluída com sucesso!"
    return render_template("categoria-delete.html")

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






    
        
    
        
        
        

    
    
    

    
    

if __name__ == '__main__':
    app.run(debug=True)