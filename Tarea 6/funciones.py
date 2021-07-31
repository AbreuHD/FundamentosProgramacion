import datetime
import db
import config
from peewee import *
import os
from prettytable import from_db_cursor
import sqlite3
import webbrowser

def verificarDatos(dato, selector):
    if (selector == 1):
        try:
            dato1 = int(input(dato))
        except:
            print("Introduce correctamente lo que se te pide")
            dato1 = verificarDatos(dato, selector)
        return dato1
    
    elif (selector == 2):
        dato1 = str(input(dato))
        if(len(dato1) == 0):
            print("Esto no puede estar vacio")
            dato1 = verificarDatos(dato, selector)
            
        for numbers in range(0,10):
            for txt in dato1:
                if(txt.find(str(numbers)) >= 0):
                    print("No se aceptan numeros")
                    dato1 = verificarDatos(dato, selector)
        return dato1
    
def ver(main):
    os.system('cls')
    connection = sqlite3.connect("vacunacion.db") 
    cursor = connection.cursor()
    cursor.execute("SELECT cedula,  nombre, apellido FROM Paciente")
    mytable = from_db_cursor(cursor)
    print(mytable)
    do = verificarDatos("Introduce 1 para ir al inicio o 2 para agregar una vacunacion: ", 1)
    if(do == 1):
        main()
    elif(do == 2):
        vacunacion(main, db.Paciente)
    else:
        input("Introduce 1 o 2... presiona enter para volver al inicio")
        main()
        

def insertVacunacion(main, cedula):
    os.system('cls')
    datab = db.Vacunacion()
    datab.idPaciente = cedula
    try:
        os.system('cls')
        connection = sqlite3.connect("vacunacion.db") 
        cursor = connection.cursor()
        cursor.execute("SELECT id, nombreProvincia FROM Provincias")
        mytable = from_db_cursor(cursor)
        print(mytable) 
        datab.idProvincia = verificarDatos("Introduce el numero de la provincia en la que se esta vacunando: ", 1)
        os.system('cls')
        connection = sqlite3.connect("vacunacion.db") 
        cursor = connection.cursor()
        cursor.execute("SELECT id, nombreVacuna, cantidadRestante FROM Vacuna")
        mytable = from_db_cursor(cursor)

        print(mytable)
        datab.idVacuna = verificarDatos("Introduce el numero de la vacuna con la que se esta vacunando: ", 1)
        getInfo = db.Vacuna.select().where(db.Vacuna.id == datab.idVacuna).get()
        if (getInfo.cantidadRestante >= 1):
            fecha = datetime.datetime.now()
            datab.fechaVacunacion = fecha.strftime('%d/%m/%Y a las %I:%M %p')
            datab.save()
            getInfo.cantidadRestante = getInfo.cantidadRestante - 1
            getInfo.save()
            input("Presiona enter para ir al inicio")
            main()
        else:
            input("No hay vacunas disponibles agrega otro cargamento en configuracion, preciona enter para ir al menu")
            main()
    except:
        input("Introduce un numero valido, presiona enter...")
        main()
def vacunacion(main, Paciente):
    os.system('cls')
    datab = Paciente()
    find = 0
    
    cedula = verificarDatos("Introduce la cedula del Paciente sin guiones: ", 1)
    
    for lista in Paciente.select():
            if (int(lista.cedula) == cedula):
                 find = 1
    if(find == 1):
        do = verificarDatos("Esta Cedula esta registrada presina 1 para agregar otra vacuna o presiona 2 para volver a escribir la cedula: ", 1)
        if(do == 1):
             insertVacunacion(main, cedula)
        elif(do == 2):
             vacunacion(main, db.Paciente)
        else:
            input("Introduce 1 o 2... presiona enter para volver al inicio")
            main()
    datab.cedula = cedula
    datab.nombre = verificarDatos("Introduce el nombre del Paciente: ", 2)
    datab.apellido = verificarDatos("Introduce el apellido del Paciente: ", 2)
    datab.save()
    insertVacunacion(main, cedula)

    do = verificarDatos("Introduce 1 para ir al inicio o 2 para agregar otra vacunacion: ", 1)
    if(do == 1):
        main()
    elif(do == 2):
        vacunacion(main, db.Paciente)
    else:
        input("Introduce 1 o 2... presiona enter para volver al inicio")
        main()
        
def Exportar(main):
    os.system('cls')
    htmlEnd = """
</body>
</html>
"""
    html = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cedula</title>
</head>
<body style="background:url(https://wallpapercave.com/wp/wp7224728.jpg); background-repeat: no-repeat; background-attachment: fixed">
    """  
    rows= db.Vacunacion.select().order_by(db.Vacunacion.idPaciente_id)
    
    nameFile = verificarDatos("Introduce el nombre del archivo: ", 2) 
    file = open(nameFile+'.html','x', encoding='utf-8')
    file.write(html)
    idName = 0
    nVacuna = 0
    testeo = 0
    try: 
        connection = sqlite3.connect("vacunacion.db") 
        cursor = connection.cursor()
        cursor.execute("SELECT idPaciente_id, idProvincia_id, idVacuna_id, fechaVacunacion FROM Vacunacion")
        mytable = from_db_cursor(cursor)
        print(mytable)

        nametest = ""
        for lista in db.Vacunacion.select().order_by(db.Vacunacion.idPaciente_id):
            nVacuna = nVacuna+1
            idP = db.Paciente.select().where(db.Paciente.cedula == lista.idPaciente_id).get()
            if(nametest != idP.cedula):
                nametest = idP.cedula
                nVacuna = 1
                file.write(f"""
        </div><p></p>  
        <div style="margin-left:auto; margin-right:auto; border-radius: 25px; border:2px solid #ffffff; width: 700px; background:linear-gradient(-30deg, rgb(146,216,33), rgb(255,255,255))">
            <h2 style="text-align: center;">Nombre: {idP.nombre}</h2>
            <h2 style="text-align: center;">Cedula: {idP.cedula}</h2>
                           """)
            idNombre = db.Vacunacion.select().where(db.Vacunacion.id == lista.id).get()
            prov = db.Vacunacion.select().where(db.Vacunacion.id == idNombre.id).get()
            provincia = db.Provincias.select().where(db.Provincias.id == prov.idProvincia_id).get()
            try:
                tipoVacuna = db.Vacuna.select().where(db.Vacuna.id == idNombre.idVacuna_id).get()
            except:
                testeo =1
                
            file.write(f"""
            <h3 style="text-align: center;">vacuna # {nVacuna}</h3>
            <h3 style="text-align: center;">Provincia: {provincia.nombreProvincia}</h3>
                           """)
            if(testeo == 0):
                file.write(f"""
            <h3 style="text-align: center;">Tipo Vacuna: {tipoVacuna.nombreVacuna}</h3>""")
            else:
                file.write(f"""
            <h3 style="text-align: center;">Tipo Vacuna: Tipo de vacuna eliminicada de la base de datos</h3>""")
                
            file.write(f"""
            <h3 style="text-align: center;">Fecha Vacuna: {prov.fechaVacunacion}</h3>""")
        file.write("""
        </div>
    <p></p>
</body>
</html>
                   """)
    
    except:
        input("Antes de exportar primero vacune a alguien")
        main()
    file.close
    webbrowser.open_new_tab(nameFile+'.html')