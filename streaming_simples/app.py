from flask import Flask, render_template
from database import get_connection, close_connection
from models.usuario import Usuario
from models.video import Video

app = Flask(__name__)
app.teardown_appcontext(close_connection)

@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/usuarios/<int:usuario_id>')
def perfil(usuario_id):
    cursor = get_connection().cursor(dictionary=True)
    usuario = Usuario(cursor).obter(usuario_id)
    cursor.close()
    if usuario is None:
        return 'Usuário não encontrado.', 404
    return render_template('perfil.html', usuario=usuario)


@app.route('/api/videos')
@app.route('/api/videos/pagina/<int:pagina>')
@app.route('/api/videos/busca/<string:termo>')
@app.route('/api/videos/busca/<string:termo>/pagina/<int:pagina>')
def buscar_videos(termo='', pagina=1):
    if pagina < 1:
        return {'erro': 'A página deve ser maior que zero.'}, 400
    cursor = get_connection().cursor(dictionary=True)
    videos = Video(cursor).buscar(termo, pagina)
    cursor.close()
    return {'pagina': pagina, 'videos': videos}


@app.route('/api/usuarios')
@app.route('/api/usuarios/busca/<string:termo>')
def buscar_usuarios(termo=''):
    cursor = get_connection().cursor(dictionary=True)
    usuarios = Usuario(cursor).buscar(termo)
    cursor.close()
    return {'usuarios': usuarios}


@app.route('/api/usuarios/<int:usuario_id>/videos')
def videos_usuario(usuario_id):
    cursor = get_connection().cursor(dictionary=True)
    usuario = Usuario(cursor).obter(usuario_id)
    if usuario is None:
        cursor.close()
        return {'erro': 'Usuário não encontrado.'}, 404
    videos = Video(cursor).por_usuario(usuario_id)
    cursor.close()
    return {'usuario': usuario, 'videos': videos}


if __name__ == '__main__':
    app.run()
