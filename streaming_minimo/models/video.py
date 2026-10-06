from database import query, execute


class Video:
    @staticmethod
    def buscar(termo, pagina, limite):
        busca = "%" + termo + "%"
        pular = (pagina - 1) * limite

        sql = """
            SELECT videos.*, usuarios.nome AS autor
            FROM videos
            JOIN usuarios ON usuarios.id = videos.usuario_id
            WHERE videos.titulo LIKE %s OR videos.descricao LIKE %s
            ORDER BY videos.id DESC
            LIMIT %s OFFSET %s
        """
        return query(sql, (busca, busca, limite, pular))

    @staticmethod
    def buscar_do_usuario(usuario_id, pagina, limite):
        pular = (pagina - 1) * limite
        sql = """
            SELECT videos.*, usuarios.nome AS autor
            FROM videos
            JOIN usuarios ON usuarios.id = videos.usuario_id
            WHERE videos.usuario_id = %s
            ORDER BY videos.id DESC
            LIMIT %s OFFSET %s
        """
        return query(sql, (usuario_id, limite, pular))

    @staticmethod
    def obter(video_id):
        dados = query("SELECT * FROM videos WHERE id = %s", (video_id,))
        return dados[0]

    @staticmethod
    def criar(titulo, descricao, arquivo, usuario_id):
        sql = """
            INSERT INTO videos (titulo, descricao, arquivo, usuario_id)
            VALUES (%s, %s, %s, %s)
        """
        return execute(sql, (titulo, descricao, arquivo, usuario_id))
