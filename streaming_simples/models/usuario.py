class Usuario:
    def __init__(self, cursor):
        self.cursor = cursor

    def buscar(self, termo):
        self.cursor.execute(
            'SELECT id, nome FROM usuarios WHERE nome LIKE %s ORDER BY id',
            ('%' + termo + '%',)
        )
        return self.cursor.fetchall()

    def obter(self, usuario_id):
        self.cursor.execute(
            'SELECT id, nome FROM usuarios WHERE id = %s',
            (usuario_id,)
        )
        return self.cursor.fetchone()
