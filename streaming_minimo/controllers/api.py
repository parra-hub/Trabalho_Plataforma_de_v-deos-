from pathlib import Path  # Caminhos de arquivos
from uuid import uuid4  # Gera nomes únicos
from flask import Blueprint, request, jsonify, current_app, send_from_directory, abort
from models.usuario import Usuario
from models.video import Video

api = Blueprint("api", __name__)  # Agrupa as rotas


# Busca vídeos
@api.get("/api/videos")
@api.get("/api/videos/busca/<string:termo>")
def buscar_videos(termo=""):
    termo = request.args.get("q", termo)  # Texto da busca
    pagina = int(request.args.get("pagina", 1))  # Página solicitada
    dados = Video.buscar(termo, pagina, 5)  # Até 5 vídeos
    return jsonify(dados)  # Devolve JSON


# Busca usuários
@api.get("/api/usuarios")
@api.get("/api/usuarios/busca/<string:termo>")
def buscar_usuarios(termo=""):
    termo = request.args.get("q", termo)
    pagina = int(request.args.get("pagina", 1))
    dados = Usuario.buscar(termo, pagina, 5)
    return jsonify(dados)


# Busca um usuário pelo ID
@api.get("/api/usuarios/<int:usuario_id>")
def obter_usuario(usuario_id):
    return jsonify(Usuario.obter(usuario_id))


# Busca os dados de um vídeo pelo ID
@api.get("/api/videos/<int:video_id>")
def obter_video(video_id):
    return jsonify(Video.obter(video_id))


# Lista os vídeos de um usuário
@api.get("/api/usuarios/<int:usuario_id>/videos")
def videos_usuario(usuario_id):
    pagina = int(request.args.get("pagina", 1))
    dados = Video.buscar_do_usuario(usuario_id, pagina, 5)
    return jsonify(dados)


# Cadastra um usuário
@api.post("/api/usuarios")
def criar_usuario():
    dados = request.get_json()  # Recebe o JSON
    usuario_id = Usuario.criar(dados["nome"])  # Salva no banco
    return jsonify(id=usuario_id), 201  # 201: criado


# Cadastra um vídeo
@api.post("/api/videos")
def criar_video():
    # Recebe os dados do formulário
    titulo = request.form["titulo"]
    descricao = request.form["descricao"]
    usuario_id = int(request.form["usuario_id"])
    arquivo = request.files["video"]

    # Verifica a extensão
    extensao = Path(arquivo.filename).suffix.lower()
    if extensao not in (".mp4", ".webm", ".ogg"):
        abort(400)

    # Gera um nome e salva o arquivo
    nome = uuid4().hex + extensao
    arquivo.save(current_app.config["UPLOAD_FOLDER"] / nome)

    # Salva os dados no banco
    video_id = Video.criar(titulo, descricao, nome, usuario_id)
    return jsonify(id=video_id), 201


# Envia o arquivo para reprodução
@api.get("/midia/<int:video_id>")
def reproduzir(video_id):
    video = Video.obter(video_id)
    return send_from_directory(
        current_app.config["UPLOAD_FOLDER"],  # Pasta
        video["arquivo"],  # Nome do arquivo
        conditional=True  # Permite solicitar partes do vídeo
    )