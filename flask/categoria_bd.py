from conexao import conecta_db

def listar_categoria(conexao):
    cursor = conexao.cursor()
    # Execução do select no banco de dados
    cursor.execute("select id,nome from categoria order by id asc")
    # recuperar todos registros
    registros = cursor.fetchall()
    for registro in registros:
        print(f"| ID: {registro[0]}  - Nome: {registro[1]} ")


def consultar_categoria_por_id(conexao):
    id = input("Digite o ID: ")
    cursor = conexao.cursor()
    cursor.execute("select id,nome from categoria where id = " + id)
    registro = cursor.fetchone()

    if registro is None:
        print("Categoria não encontrada :")
    else:
        print(f"| ID ..: {registro[0]} ")
        print(f"| Nome : {registro[1]} ")


def inserir_categoria(conexao, nome):
    cursor = conexao.cursor()
    sql_insert = "insert into categoria (nome) values ('" + nome + "')"
    cursor.execute(sql_insert)
    conexao.commit()

def atualizar_categoria(conexao):
    print("Alterando dados dos Categoria")
    cursor = conexao.cursor()
    id   = input("Digite o ID : ")
    nome = input("Nome :")
    sql_update = "update categoria set nome ='" + nome + "' where id = "+ id
    cursor.execute(sql_update)
    conexao.commit()

def deletar_categoria(conexao):
    print("Deletando Categoria")
    cursor = conexao.cursor()
    id   = input("Digite o ID : ")
    sql_delete = "delete from categoria where id = "+ id
    cursor.execute(sql_delete)
    conexao.commit()