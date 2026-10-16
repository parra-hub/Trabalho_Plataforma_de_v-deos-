class Usuario:
    def __init__(self, cursor):
        self.cursor = cursor

    def buscar(self, termo, pagina=1):
        inicio = (pagina - 1) * 5
        self.cursor.execute(
            'SELECT id, nome FROM usuarios WHERE nome LIKE %s ORDER BY id LIMIT 5 OFFSET %s',
            ('%' + termo + '%', inicio)
        )
        return self.cursor.fetchall()

    def obter(self, usuario_id):
        self.cursor.execute(
            'SELECT id, nome FROM usuarios WHERE id = %s',
            (usuario_id,)
        )
        return self.cursor.fetchone()
