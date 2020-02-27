import sqlite3

# abrindo conexão com bd
conn = sqlite3.connect('locadora.db')

# definindo um cursor para manipular os registros do bd
cursor = conn.cursor()

# criando a tabela
cursor.execute("""
CREATE TABLE tipo (
IdTipo INTEGER PRIMARY KEY AUTOINCREMENT,
Tipo VARCHAR(10)
);

CREATE TABLE usuarios (
IdUsuario INTEGER PRIMARY KEY AUTOINCREMENT,
Nome VARCHAR(20),
Senha VARCHAR(10),
TipoId INTEGER,
DataCadastro DATETIME
FOREIGN KEY (TipoId) REFERENCES tipo(IdTipo)
);

CREATE TABLE clientes (
IdCliente INTEGER PRIMARY KEY AUTOINCREMENT,
Nome VARCHAR(),
CPF INTEGER,
UsuarioId INTEGER,
DataCadastro DATETIME,
FOREIGN KEY (UsuarioId) REFERENCES usuarios(IdUsuario)
);


CREATE TABLE alugueis (
IdAluguel INTEGER PRIMARY KEY AUTOINCREMENT,
Carro INTEGER,
ClienteId INTEGER,
FOREIGN KEY(ClienteId) REFERENCES clientes(IdCliente)
);

CREATE TABLE carros (
IdCarro INTEGER PRIMARY KEY AUTOINCREMENT,
Nome VARCHAR(30),
Marca VARCHAR(20),
KmAtual INTEGER,
UsuarioId INTEGER,
Alugado BOOLEAN,
DataCadastro DATETIME,
FOREIGN KEY(UsuarioId) REFERENCES usuarios(IdUsuario)
);

""")

conn.close()