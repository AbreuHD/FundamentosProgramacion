from peewee import *

databasee = SqliteDatabase('AnimeData.db')

class Animes(Model):
    nombreAnime = CharField()
    cantidadPersonaje = IntegerField()
    class Meta:
        database = databasee

class Personajes(Model):
    nombre = CharField()
    apellido = CharField()
    foto = CharField()
    pronunciacion = CharField()
    serie = CharField()
    nacimiento = DateField()
    zodiaco = CharField()
    poder = CharField()
    fraseFav = CharField()
    descripcionR = CharField()
    edad = CharField()
    altura = IntegerField()
    sexo = CharField(max_length=1)
    estado = CharField()
    lat = FloatField()
    lng = FloatField()
    direccion = CharField()    
    class Meta:
        database = databasee
        
databasee.connect()
databasee.create_tables([Animes, Personajes])