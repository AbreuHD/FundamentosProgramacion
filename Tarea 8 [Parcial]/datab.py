from peewee import *

databasee = SqliteDatabase('Robos.db')

class Robo(Model):
    cedula = IntegerField()
    nombre = CharField(20)
    fecha = DateTimeField()
    objetoRobado = CharField(20)
    valor = IntegerField()
    lugar = CharField(30)
    lat = DoubleField()
    lng = DateTimeField()
    class Meta:
        database = databasee

databasee.connect()
databasee.create_tables([Robo])