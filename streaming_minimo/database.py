import mysql.connector


def conectar():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="99802@Gabi",
        database="streaming_simples"
    )


# Executa um SELECT e devolve uma lista de registros.
def query(sql, parametros=()):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute(sql, parametros)
        return cursor.fetchall()
    finally:
        cursor.close()
        conexao.close()


# Executa um INSERT e devolve o ID criado.
def execute(sql, parametros):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute(sql, parametros)
        conexao.commit()
        return cursor.lastrowid
    finally:
        cursor.close()
        conexao.close()
