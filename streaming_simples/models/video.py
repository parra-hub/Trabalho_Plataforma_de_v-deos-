class Video:
    def __init__(self, cursor):
        self.cursor = cursor

    def buscar(self, termo, pagina):
        # Cada página mostra até cinco vídeos.
        inicio = (pagina - 1) * 5
        pesquisa = '%' + termo + '%'
        self.cursor.execute('''
            SELECT videos.id, videos.titulo, videos.descricao,
                   videos.arquivo, videos.usuario_id, usuarios.nome AS autor
            FROM videos JOIN usuarios ON videos.usuario_id = usuarios.id
            WHERE videos.titulo LIKE %s OR videos.descricao LIKE %s
            ORDER BY videos.id LIMIT 5 OFFSET %s
        ''', (pesquisa, pesquisa, inicio))
        return self.cursor.fetchall()

    def por_usuario(self, usuario_id):
        self.cursor.execute('''
            SELECT videos.id, videos.titulo, videos.descricao,
                   videos.arquivo, videos.usuario_id, usuarios.nome AS autor
            FROM videos JOIN usuarios ON videos.usuario_id = usuarios.id
            WHERE videos.usuario_id = %s ORDER BY videos.id
        ''', (usuario_id,))
        return self.cursor.fetchall()
