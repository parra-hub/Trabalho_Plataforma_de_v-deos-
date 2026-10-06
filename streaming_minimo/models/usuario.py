from database import query, execute


class Usuario:
    @staticmethod
    def buscar(termo, pagina, limite):
        busca = "%" + termo + "%"
        pular = (pagina - 1) * limite

        sql = """
            SELECT id, nome FROM usuarios
            WHERE nome LIKE %s
            ORDER BY id DESC
            LIMIT %s OFFSET %s
        """
        return query(sql, (busca, limite, pular))

    @staticmethod
    def obter(usuario_id):
        dados = query(
            "SELECT id, nome FROM usuarios WHERE id = %s",
            (usuario_id,)
        )
        return dados[0]

    @staticmethod
    def criar(nome):
        return execute(
            "INSERT INTO usuarios (nome) VALUES (%s)",
            (nome,)
        )
