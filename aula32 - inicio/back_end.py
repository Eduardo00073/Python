import sqlite3 as sql


# criando um banco de dados
banco = sql.connect("lista.db")


def inserir(valor):
    with banco:
        cursor = banco.cursor()
        comando_insert = "INSERT INTO tarefas(nome) VALUES(?)"
        cursor.execute(comando_insert, valor)


def buscar():
    lista_afazeres = []
    with banco:
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM tarefas")

        linha = cursor.fetchall()
        for linhas in linha:
            lista_afazeres.append(linhas)

    return lista_afazeres


def deletar(valor):
    with banco:
        cursor = banco.cursor()
        comando_delete = "DELETE FROM tarefas WHERE id=?"
        cursor.execute(comando_delete, valor)


def atualizar(valor):
    with banco:
        cursor = banco.cursor()
        comando_atualizar = "UPDATE tarefas SET nome=? WHERE id=?"
        cursor.execute(comando_atualizar, valor)
