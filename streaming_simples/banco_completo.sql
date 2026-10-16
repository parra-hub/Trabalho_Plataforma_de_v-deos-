CREATE DATABASE streaming_novo CHARACTER SET utf8mb4;

USE streaming_novo;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE videos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    descricao TEXT NOT NULL,
    arquivo VARCHAR(200) NOT NULL,
    usuario_id INT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

INSERT INTO usuarios (nome)
VALUES ('Ana'), ('Bruno'), ('Carla'), ('Diego'), ('Elisa'), ('Felipe');

INSERT INTO videos (titulo, descricao, arquivo, usuario_id)
VALUES
('Python - exemplo 1',
 'Clipe de demonstração para buscar Python.',
 'video1.mp4', 1),

('Flask - exemplo 2',
 'Clipe de demonstração para buscar Flask.',
 'video2.mp4', 1),

('Rotas - exemplo 3',
 'Clipe de demonstração de uma rota.',
 'video3.mp4', 1),

('HTML - exemplo 4',
 'Clipe de demonstração para buscar HTML.',
 'video4.mp4', 2),

('MySQL - exemplo 5',
 'Clipe de demonstração para buscar MySQL.',
 'video5.mp4', 2),

('Python - exemplo 6',
 'Clipe de demonstração para testar a segunda página.',
 'video6.mp4', 2);