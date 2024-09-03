import sqlite3 as sql


# criando um banco de dados
banco = sql.connect("lista.db")


def inserir(valor):
    with banco:
        cursor = banco.cursor()
        comando_insert = "INSERT INTO tarefas(nome) VALUES(?)"
        cursor.execute(comando_insert, valor)
