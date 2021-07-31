from peewee import *
import os
from prettytable import from_db_cursor
import sqlite3
import webbrowser
from playsound import playsound


db = SqliteDatabase('listaEstudiantes.db')

class listadoEstudiante(Model):
   matriculaEstudiante = IntegerField()
   nombreEstudiante = CharField(50)
   apellidoEstudiante = CharField(50)
   n1 = IntegerField()
   n2 = IntegerField()
   calificacion = CharField(1)
   class Meta:
       database = db
       
db.connect()
db.create_tables([listadoEstudiante])
    

def agregar(main):
    os.system('cls')
    playsound('sound/agregar old.mp3')
    tabla = listadoEstudiante()
    find = 0
    matriculacion = int(input("Introduce la matricula sin guiones: "))
    
    for lista in listadoEstudiante.select():
        if (lista.matriculaEstudiante == matriculacion): 
            find = 1
    
    if (find == 1):
        validator = int(input("Ya existe un estudiante con esa matricula... presiona 1 si quieres modificar su info o presiona 0 para ir al inicio: "))
        if (validator == 1):
            modificar(main)
        elif (validator == 0):
            main()
    tabla.matriculaEstudiante = matriculacion
    tabla.nombreEstudiante = str(input("Introduce el nombre del estudiante: "))
    tabla.apellidoEstudiante = str(input("Introduce el apellido del estudiante: "))
    tabla.n1 = int(input("Introduce la primera calicacion: "))
    tabla.n2 = int(input("Introduce la segunda calificacion: "))
    if ((tabla.n1+tabla.n2)/2 >= 90):
        tabla.calificacion = 'A'
    elif ((tabla.n1+tabla.n2)/2 >= 80):
        tabla.calificacion = 'B'
    elif ((tabla.n1+tabla.n2)/2 >= 70):
        tabla.calificacion = 'C'
    else : tabla.calificacion = 'F'
    tabla.save()
    validate = int(input("Cambios efectuados, preciona 1 para ver los datos, 2 para ir al inicio y 3 para agregar otro estudiante: "))
    if (validate == 1): mostrar(main)
    elif (validate == 2): main()
    elif (validate == 3): agregar(main)
    else: 
        input("Introduce un numero valido, presiona enter para ir al inicio ")
        main()

def mostrar(main):
    os.system('cls')
    playsound('sound/MostrarOld.mp3')
    connection = sqlite3.connect("listaEstudiantes.db")
    cursor = connection.cursor() 
    cursor.execute("SELECT matriculaEstudiante, nombreEstudiante, apellidoEstudiante, n1, n2, calificacion FROM listadoEstudiante")
    mytable = from_db_cursor(cursor)
    print(mytable)
    do = int(input("Preciona 1 si quieres ir al inicio, preciona 2 si quieres salir "))
    if (do == 1):
        input("Preciona enter para ir al inicio ")
        main()
    elif (do == 2):
        print("Ok... Saliendo")
    else:
        input("Introduce un numero valido, presiona enter para continuar ")
        main()

def modificar(main):
    os.system('cls')
    playsound('sound/modificar old.mp3')
    find = 0
    connection = sqlite3.connect("listaEstudiantes.db")
    cursor = connection.cursor()
    cursor.execute("SELECT matriculaEstudiante, nombreEstudiante, apellidoEstudiante, n1, n2, calificacion FROM listadoEstudiante")
    mytable = from_db_cursor(cursor)
    print(mytable)
    playsound('sound/Modificar0.mp3')
    id = input("Introduce la matricula del estudiante que quieres modificar o introduce 0 para cancerlar: ")
    
    if (id.capitalize != 0):
        for lista in listadoEstudiante.select():
            if (int(lista.matriculaEstudiante) == int(id)):
                 find = 1
            
    if (id.capitalize == 0):
        print("Ok... Retornando al inicio") 
    elif (id.capitalize != 0 and find == 1):
        tabla = listadoEstudiante.select().where(listadoEstudiante.matriculaEstudiante == id).get()
        print("Pon un 0 si no quieres realizar cambios")
        newM = int(input("Introduce la nueva matricula: "))
        newN = str(input("Introduce el nuevo nombre: "))
        newA = str(input("Introduce la nueva apellido: "))
        newC1 = int(input("Introduce la nueva calificacion 1: "))
        newC2 = int(input("Introduce la nueva Calificacion 2: "))
        
        if (newM == 0): newM = tabla.matriculaEstudiante
        if (newN == "0"): newN = tabla.nombreEstudiante
        if (newA == "0"): newA = tabla.apellidoEstudiante
        if (newC1 == 0): newC1 = tabla.n1
        if (newC2 == 0): newC2 = tabla.n2
        
        if ((newC1+newC2)/2 >= 90):
            newCali = 'A'
        elif ((newC1+newC2)/2 >= 80):
            newCali = 'B'
        elif ((newC1+newC2)/2 >= 70):
          newCali = 'C'
        else : newCali = 'F'
        playsound('sound/ConfimarModificacionOld.mp3')
        print(f"""
              Vas a cambiar los siguientes datos... Estas seguro? Escribe CONFIRMAR (En Mayusculas) para confirmar.
              
                            Matricula: {tabla.matriculaEstudiante} ---> {newM}
                            Nombre: {tabla.nombreEstudiante} ---> {newN}
                            Apellido: {tabla.apellidoEstudiante} ---> {newA}
                            Calificacion 1: {tabla.n1} ---> {newC1}
                            Calificacion 2: {tabla.n2} ---> {newC2}
                            Calificacion literal: {tabla.calificacion} ----> {newCali}
                            
              """)
        confirm = str(input())
        if (confirm == "CONFIRMAR"):
            tabla.matriculaEstudiante = newM
            tabla.nombreEstudiante = newN
            tabla.apellidoEstudiante = newA
            tabla.n1 = newC1
            tabla.n2 = newC2
            tabla.calificacion = newCali
            tabla.save()
            validate = int(input("Cambios efectuados, preciona 1 para ver los datos y 2 para ir al inicio "))
            if (validate == 1): mostrar(main)
            elif (validate == 2): main()
            else: 
                input("Introduce un numero valido, presiona enter para ir al inicio ")
                main()
        else: 
            input("Datos no efectuados, preciona enter para continuar e ir al inicio ")
            main()
    else: 
        input("Introduce una matricula valida, preciona enter para ir al inicio ")
        main()

    
def eliminar(main):
    os.system('cls')
    playsound('sound/Eliminar Old.mp3')
    connection = sqlite3.connect("listaEstudiantes.db")
    cursor = connection.cursor()
    cursor.execute("SELECT matriculaEstudiante, nombreEstudiante, apellidoEstudiante, n1, n2, calificacion FROM listadoEstudiante")
    mytable = from_db_cursor(cursor)
    print(mytable)
        
    id = input("Introduce la matricula del estudiante que quieres eliminar o introduce 0 para cancerlar: ")
    find = 0
    
    if (id.capitalize != 0):
        for lista in listadoEstudiante.select():
            if (lista.matriculaEstudiante == int(id)): 
               find = 1
    
    if (id.capitalize == 0):
        print("Ok... Retornando al inicio")
    elif (find == 1):
        tabla = listadoEstudiante.select().where(listadoEstudiante.matriculaEstudiante == id).get()
        print(f" Piensas borrar {tabla.matriculaEstudiante} ║ {tabla.nombreEstudiante} Estas seguro?")
        playsound('sound/ConfirmarEliminarOld.mp3')
        confirm = str(input("Introduce CONFIRMAR en mayusculas para confirmar: "))
        if (confirm == "CONFIRMAR"):
            print(f" {tabla.matriculaEstudiante} ║ {tabla.nombreEstudiante} fue borrado")
            tabla.delete_instance()
            validate = int(input("Cambios efectuados, preciona 1 para ver los datos y 2 para ir al inicio "))
            if (validate == 1): mostrar(main)
            elif (validate == 2): main()
            else: 
                input("Introduce un numero valido, presiona enter para ir al inicio ")
                main()
            
    else: 
        input("Introduce una matricula existente, presiona enter para continuar e ir al inicio")
        main()
    
def exportar():
    os.system('cls')
    playsound('sound/Exportar Old.mp3')
    connection = sqlite3.connect("listaEstudiantes.db")
    cursor = connection.cursor()
    cursor.execute("SELECT matriculaEstudiante, nombreEstudiante, apellidoEstudiante, n1, n2, calificacion FROM listadoEstudiante")
    databaseForHTML = from_db_cursor(cursor)
    databaseForHTML = databaseForHTML.get_html_string()
    databaseForHTML = databaseForHTML.replace('<table>', '<table class="table table-bordered>"').replace('matriculaEstudiante', 'Matricula').replace('nombreEstudiante','Nombre').replace('apellidoEstudiante','Apellido').replace('n1', 'Nota 1').replace('n2','Nota 2').replace('calificacion','Calificacion Literal')
    htmlGG = f"""
    
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <title>Database</title>
</head>
<body>
    <div class = 'container'>
        {databaseForHTML}
    </dib>
</body>
</html>
    """
    nameF = str(input("Con que nombre quieres exportar la tabla? "))
    file = open(nameF+'.html', 'x')
    file.write(htmlGG)
    file.close()
    webbrowser.open(nameF+'.html')