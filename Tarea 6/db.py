from peewee import *
from prettytable import from_db_cursor


datab = SqliteDatabase('vacunacion.db')

class Paciente(Model):
   cedula = IntegerField()
   nombre = CharField(50)
   apellido = CharField(50)
   class Meta:
       database = datab
       
class Provincias(Model):
   nombreProvincia = TextField() 
   class Meta:
       database = datab
       
class Vacuna(Model):
   nombreVacuna = CharField(50)
   cantidadRestante = IntegerField()
   class Meta:
       database = datab
       
class Vacunacion(Model):
   idPaciente = ForeignKeyField(Paciente, backref='idPaciente')
   idProvincia = ForeignKeyField(Provincias, backref='idProvincia')
   idVacuna = ForeignKeyField(Vacuna, backref='idVacuna')
   fechaVacunacion = DateTimeField()
   class Meta:
       database = datab
       
datab.connect()
datab.create_tables([Paciente, Provincias, Vacuna, Vacunacion])

def Introducir(info, selector):
    if(selector == 1):
        db = Provincias()
        db.nombreProvincia = str(i)
        db.save()
    elif(selector == 0):
        db = Vacuna()
        db.nombreVacuna = str(i)
        db.cantidadRestante = 25
        db.save()
    return

try: 
    proT = Provincias.select().where(Provincias.id == 1).get()
except:
    provinciasList = ['Azua', 'Bahoruco', 'Barahona', 'Dajabón', 'Distrito Nacional', 'Duarte', 'Elías Piña', 'El Seibo', 'Espaillat', 'Hato Mayor', 'Hermanas Mirabal', 'Independencia', 'La Altagracia', 'La Romana', 'La Vega', 'María Trinidad Sánchez', 'Monseñor Nouel', 'Monte Cristi', 'Monte Plata', 'Pedernales', 'Peravia', 'Puerto Plata', 'Samaná', 'Sánchez Ramírez', 'San Cristóbal', 'San José de Ocoa', 'San Juan', 'San Pedro de Macorís', 'Santiago', 'Santiago Rodríguez', 'Santo Domingo', 'Valverde']
    for i in  provinciasList:
        Introducir(i,1)
        
try: 
    proT = Vacuna.select().where(Vacuna.id == 1).get()
except:
    vacunaList = ['Pfizer', 'Moderna', 'Astrazeneca', 'Janssen']
    for i in  vacunaList:
        Introducir(i,0)