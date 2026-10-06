from pathlib import Path
from flask import Flask, render_template
from controllers.api import api

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = Path(app.root_path) / "uploads" #Defini a pasta dos vídeos.
app.config["UPLOAD_FOLDER"].mkdir(exist_ok=True) #Cria a pasta uploads caso não exista 
app.config["MAX_CONTENT_LENGTH"] = 100 * 1024 * 1024 #Limita o tamanho máximo do vídeo na hora do upload 
app.register_blueprint(api) #Conecta as rotas do api.py a aplicação flask 


@app.get("/") #Inicia a pagina inicial index.html 
def inicio():
    return render_template("index.html")


@app.get("/usuarios/<int:usuario_id>")
def perfil(usuario_id):
    return render_template("perfil.html", usuario_id=usuario_id)


if __name__ == "__main__":
    app.run()
