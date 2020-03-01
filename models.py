import db
import peewee
import datetime
from flask_login import UserMixin
""" 
    No peewee não é preciso identificar a chave
    primaria na criação, ele já cria um campo
    com auto incremento para chave primaria
    automaticamente.
"""

class Tipo(db.BaseModel):
    # Classe representa a tabela Tipo
    # A tabela possui o campo 'tipo', para saber qual tipo de usuario está acessando
    tipo = peewee.CharField(unique=True)

class Usuarios(db.BaseModel):
    # Classe representa a tabela Usuarios
    
    nome = peewee.CharField(unique=True, max_length=20,null=False)
    senha = peewee.CharField(max_length=10, null=False)
    # Chave estrangeira da tabela tipo
    tipo = peewee.ForeignKeyField(Tipo)
    dataCadastro = peewee.DateTimeField(default=datetime.datetime.now)

class Clientes(db.BaseModel, UserMixin):
    # Classe que representa a tabela clientes

    nome = peewee.CharField(null=False)
    cpf = peewee.CharField(null=False)
    # Chave estrangeira da tabela usuarios para identificar o usuario que efetuou o cadastro do cliente
    usuario = peewee.ForeignKeyField(Usuarios)
    dataCadastro = peewee.DateTimeField(default=datetime.datetime.now)

class Carros(db.BaseModel):
    # Classe que representa a tabela Carros

    nome = peewee.CharField(null=False)
    marca = peewee.CharField(null=False)
    kmAtual = peewee.IntegerField(null=False)
    usuario = peewee.ForeignKeyField(Usuarios)
    alugado = peewee.BooleanField(null=False)
    dataCadastro = peewee.DateTimeField(default=datetime.datetime.now)

class Alugueis(db.BaseModel):
    # Classe que representa a tabela Alugueis

    carro = peewee.ForeignKeyField(Carros)
    cliente = peewee.ForeignKeyField(Clientes)
    dataCadastro = peewee.DateTimeField(default=datetime.datetime.now)


if __name__ == '__main__':
    try:
        Tipo.create_table()
        print("1º")
    except peewee.OperationalError:
        print("Erro Tipo")
    try:
        Usuarios.create_table()
        print("2º")
    except peewee.OperationalError:
        print("Errp Usuarios")
    try:
        Clientes.create_table()
        print("3º")
    except peewee.OperationalError:
        print("Erro Clientes")
    try:
        Carros.create_table()
        print("4º")
    except peewee.OperationalError:
        print("Erro Carros")
    try:
        Alugueis.create_table()
        print("5º")
    except peewee.OperationalError:
        print("Erro Alugueis")