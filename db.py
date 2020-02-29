import peewee

db = peewee.SqliteDatabase('locadora.db')

class BaseModel(peewee.Model):
    """Classe model base"""

    class Meta:
        # cria a conexão com o bd
        database = db