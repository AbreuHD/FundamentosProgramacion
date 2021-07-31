from peewee import *
import peewee

databasee = SqliteDatabase('motores.db')

class User(Model):
   cedula = IntegerField()
   nombre = CharField(50)
   telefono = IntegerField()
   direccion = CharField(50)
   act = CharField(50)
   class Meta:
       database = databasee

class Motos(Model):
   idUser = ForeignKeyField(User, backref='idUser')
   marca = CharField(50)
   modelo = CharField(50)
   placa = CharField(50)
   chasis = CharField(50)
   lat = DoubleField()
   lng = DoubleField()
   descripcion = CharField(50)
   class Meta:
       database = databasee
       
databasee.connect()
databasee.create_tables([User, Motos])