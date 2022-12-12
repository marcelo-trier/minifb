SHOW DATABASES;

CREATE DATABASE dbMinifb;
USE dbMinifb;
CREATE TABLE tbUsuario (
	id int primary key auto_increment,
    nome varchar(70),
    email varchar(70),
    apelido varchar(25),
    senha varchar(50),
    imagem varchar(250)
);

CREATE TABLE tbMensagem (
	id int primary key auto_increment,
    mensagem varchar(250) not null,
    id_usuario int not null,
    
    FOREIGN KEY(id_usuario) REFERENCES tbUsuario(id)
);

CREATE TABLE tbAmigo (
	id int primary key auto_increment,
    id_usuario int not null,
    id_amigo int not null,
    
    FOREIGN KEY(id_usuario) REFERENCES tbUsuario(id),
    FOREIGN KEY(id_amigo) REFERENCES tbUsuario(id)
);


INSERT INTO tbUsuario(nome,email,apelido,senha,imagem)
	VALUES
    ('Marcelo Pereira', 'pereira@email.com', 'pereira', 'abc123', 'pereira.jpg'),
    ('Jimmy Hendrix', 'hendrix@email.com', 'jimmy', '123abc', 'hendrix.jpg');

SELECT * from tbUsuario;
INSERT INTO tbAmigo(id_usuario,id_amigo)
	VALUES (1, 2);


INSERT INTO tbMensagem(mensagem,id_usuario)
	VALUES
    ('hoje vou tocar guitarra', 2),
    ('hoje vou programar', 1);

SELECT * from tbMensagem
	JOIN tbUsuario ON tbUsuario.id = tbMensagem.id_usuario
    WHERE nome LIKE 'marcelo%';

