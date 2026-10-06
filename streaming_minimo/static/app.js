let paginaVideo = 1;
let paginaUsuario = 1;
let termoVideo = "";
let termoUsuario = "";
const perfil = document.getElementById("perfil");

async function carregarVideos() {
    let rota = "/api/videos";
    if (perfil) {
        rota = "/api/usuarios/" + perfil.dataset.id + "/videos";
    }

    const resposta = await fetch(rota + "?pagina=" + paginaVideo + "&q=" + encodeURIComponent(termoVideo));
    const videos = await resposta.json();
    const lista = document.getElementById("videos");
    lista.replaceChildren();

    for (const video of videos) {
        const modelo = document.getElementById("modelo-video");
        const item = modelo.content.cloneNode(true);
        item.querySelector("h3").textContent = video.titulo;
        item.querySelector("p").textContent = video.descricao;
        item.querySelector("a").textContent = video.autor;
        item.querySelector("a").href = "/usuarios/" + video.usuario_id;
        item.querySelector("video").src = "/midia/" + video.id;
        lista.append(item);
    }

    if (videos.length === 0) {
        lista.textContent = "Nenhum vídeo encontrado.";
    }
    document.getElementById("pagina-video").textContent = "Página " + paginaVideo;
    document.getElementById("anterior-video").disabled = paginaVideo === 1;
    document.getElementById("proximo-video").disabled = videos.length < 5;
}

function buscarVideos(evento) {
    evento.preventDefault();
    termoVideo = document.getElementById("busca-video").value;
    paginaVideo = 1;
    carregarVideos();
}

function mudarVideos(valor) {
    paginaVideo = paginaVideo + valor;
    carregarVideos();
}

async function carregarUsuarios() {
    const resposta = await fetch("/api/usuarios?pagina=" + paginaUsuario + "&q=" + encodeURIComponent(termoUsuario));
    const usuarios = await resposta.json();
    const lista = document.getElementById("usuarios");
    const autores = document.getElementById("autor");
    lista.replaceChildren();
    autores.replaceChildren(new Option("Selecione um autor", ""));

    for (const usuario of usuarios) {
        const item = document.createElement("li");
        const link = document.createElement("a");
        link.textContent = usuario.nome;
        link.href = "/usuarios/" + usuario.id;
        item.append(link);
        lista.append(item);
        autores.add(new Option(usuario.nome, usuario.id));
    }

    if (usuarios.length === 0) {
        lista.textContent = "Nenhum usuário encontrado.";
    }
    document.getElementById("pagina-usuario").textContent = "Página " + paginaUsuario;
    document.getElementById("anterior-usuario").disabled = paginaUsuario === 1;
    document.getElementById("proximo-usuario").disabled = usuarios.length < 5;
}

function buscarUsuarios(evento) {
    evento.preventDefault();
    termoUsuario = document.getElementById("busca-usuario").value;
    paginaUsuario = 1;
    carregarUsuarios();
}

function mudarUsuarios(valor) {
    paginaUsuario = paginaUsuario + valor;
    carregarUsuarios();
}

async function cadastrarUsuario(evento) {
    evento.preventDefault();
    const formulario = evento.target;
    const resposta = await fetch("/api/usuarios", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({nome: formulario.elements.nome.value})
    });
    if (resposta.ok) {
        formulario.reset();
        termoUsuario = "";
        paginaUsuario = 1;
        document.getElementById("busca-usuario").value = "";
        await carregarUsuarios();
        alert("Usuário cadastrado.");
    }
}

async function publicarVideo(evento) {
    evento.preventDefault();
    const formulario = evento.target;
    const botao = formulario.querySelector("button");
    botao.disabled = true;
    botao.textContent = "Enviando...";
    const resposta = await fetch("/api/videos", {
        method: "POST",
        body: new FormData(formulario)
    });
    botao.disabled = false;
    botao.textContent = "Publicar";
    if (resposta.ok) {
        formulario.reset();
        termoVideo = "";
        paginaVideo = 1;
        document.getElementById("busca-video").value = "";
        await carregarVideos();
        alert("Vídeo publicado.");
    }
}

async function iniciar() {
    if (perfil) {
        const resposta = await fetch("/api/usuarios/" + perfil.dataset.id);
        const usuario = await resposta.json();
        perfil.textContent = "Vídeos de " + usuario.nome;
    } else {
        carregarUsuarios();
    }
    carregarVideos();
}

iniciar();
