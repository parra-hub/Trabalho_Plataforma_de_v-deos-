
async function consultar(url) {
    document.querySelector('#erro').textContent = '';
    try {
        const resposta = await fetch(url);
        if (resposta.ok) {
            return await resposta.json();
        }
    } catch (erro) {
        
    }
    document.querySelector('#erro').textContent = 'Não foi possível consultar a API. Confira o servidor e o banco.';
    return null;
}

async function buscarVideos() {
    const termo = document.querySelector('#termo-video').value.trim();
    const pagina = document.querySelector('#pagina').value;
    let url = '/api/videos';
    if (termo !== '') {
        url += '/busca/' + encodeURIComponent(termo);
    }
    const dados = await consultar(url + '/pagina/' + pagina);
    if (dados !== null) {
        mostrarVideos(dados.videos);
    }
}

async function buscarUsuarios() {
    const termo = document.querySelector('#termo-usuario').value.trim();
    let url = '/api/usuarios';
    if (termo !== '') {
        url += '/busca/' + encodeURIComponent(termo);
    }
    const dados = await consultar(url);
    if (dados === null) {
        return;
    }
    const lista = document.querySelector('#usuarios');
    lista.textContent = 'Nenhum usuário encontrado.';
    if (dados.usuarios.length > 0) {
        lista.textContent = '';
    }
    for (const usuario of dados.usuarios) {
        const item = document.createElement('li');
        const link = document.createElement('a');
        link.textContent = usuario.nome;
        link.href = '/usuarios/' + usuario.id;
        item.append(link);
        lista.append(item);
    }
}

async function carregarPerfil(id) {
    const dados = await consultar('/api/usuarios/' + id + '/videos');
    if (dados !== null) {
        mostrarVideos(dados.videos);
    }
}

function mostrarVideos(videos) {
    const lista = document.querySelector('#videos');
    lista.textContent = 'Nenhum vídeo encontrado.';
    if (videos.length > 0) {
        lista.textContent = '';
    }
    for (const video of videos) {
        const item = document.createElement('article');
        const titulo = document.createElement('h3');
        titulo.textContent = video.titulo;
        const descricao = document.createElement('p');
        descricao.textContent = video.descricao;
        const autor = document.createElement('a');
        autor.textContent = video.autor;
        autor.href = '/usuarios/' + video.usuario_id;
        const player = document.createElement('video');
        player.controls = true;
        player.preload = 'metadata';
        player.src = '/static/videos/' + encodeURIComponent(video.arquivo);
        item.append(titulo, descricao, autor, player);
        lista.append(item);
    }
}
