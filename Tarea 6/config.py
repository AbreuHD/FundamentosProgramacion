import datetime
import db
from peewee import *
import os
from prettytable import from_db_cursor
import sqlite3

def configuracion(main, funciones):
          os.system('cls')
          print("""
            ╔═════════════════════════════════════════════════════════════════════════════╗
            ║                                                                             ║
            ║                  ░█████╗░░█████╗░███╗░░██╗███████╗██╗░██████╗░              ║
            ║                  ██╔══██╗██╔══██╗████╗░██║██╔════╝██║██╔════╝░              ║
            ║                  ██║░░╚═╝██║░░██║██╔██╗██║█████╗░░██║██║░░██╗░              ║
            ║                  ██║░░██╗██║░░██║██║╚████║██╔══╝░░██║██║░░╚██╗              ║
            ║                  ╚█████╔╝╚█████╔╝██║░╚███║██║░░░░░██║╚██████╔╝              ║
            ║                  ░╚════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░░░░╚═╝░╚═════╝░              ║  
            ║                                                                             ║
            ║≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈║
            ║               Introduce un numero para hacer dicha accion.                  ║
            ║                                                                             ║
            ║                                1 = Provincias                               ║
            ║                                2 = Vacunas                                  ║
            ║                                3 = Inicio                                   ║
            ║                                                                             ║
            ╚═════════════════════════════════════════════════════════════════════════════╝ 
           """)
          selector = funciones.verificarDatos(": ", 1)
          if (selector == 1):
              Provincias(main, funciones)
          elif (selector == 2):
              Vacunas(main, funciones)
          elif (selector == 3):
              main()
          else: 
              input("Solo son validos los numeros del 1 al 3, presiona enter para volver a intentarlo")
              configuracion(main, funciones)



def Provincias(main, funciones):           
    os.system('cls')
    connection = sqlite3.connect("vacunacion.db") 
    cursor = connection.cursor()
    cursor.execute(f"SELECT id, nombreProvincia FROM Provincias")
    mytable = from_db_cursor(cursor)
    print(mytable)
    do = funciones.verificarDatos("Introduce 1 para ir al inicio o 2 para agregar una vacunacion: ", 1)
    if(do == 1):
        main()
    elif(do == 2):
        funciones.vacunacion(main, db.Paciente)
    else:
        input("Introduce 1 o 2... presiona enter para volver al inicio")
        main()

def Vacunas(main, funciones):
    os.system('cls')
    connection = sqlite3.connect("vacunacion.db") 
    cursor = connection.cursor()
    cursor.execute(f"SELECT id, nombreVacuna, cantidadRestante FROM Vacuna")
    mytable = from_db_cursor(cursor)
    print(mytable)
    do = funciones.verificarDatos("Introduce 1 para ir al inicio o 2 para modificar o agregar vacunas: ", 1)
    if(do == 1):
        main()
    elif(do == 2):
        ModificarVacuna(main, funciones, Vacunas)
    else:
        input("Introduce 1 o 2... presiona enter para volver al inicio")
        main()
        
def ModificarVacuna(main, funciones, Vacunas):
    os.system('cls')
    find = 0
    id = 0
    selector = funciones.verificarDatos("Presiona 1 si quieres alguna vacuna, 2 si llego un cargamento de vacunas o 3 si quieres añadir un tipo nuevo de vacuna y 4 si quieres eliminar alguna: ", 1)
    if(selector == 1):
        connection = sqlite3.connect("vacunacion.db") 
        cursor = connection.cursor()
        cursor.execute(f"SELECT id, nombreVacuna, cantidadRestante FROM Vacuna")
        mytable = from_db_cursor(cursor)
        print(mytable)
        id = funciones.verificarDatos("Introduce el ID de la vacuna a modificar", 1)
        
        for i in db.Vacuna.select():
            if (int(i.id) == int(id)):
                    find = 1
        if(find == 1):
            dbEdit = db.Vacuna.select().where(db.Vacuna.id == id).get()
            nombreNew = funciones.verificarDatos("Introduce el nuevo nombre: ", 2)
            cantidadNew = funciones.verificarDatos("Cuantas vacunas hay?: ", 1)
            print(f"""
                  Los cambios son:
                  {dbEdit.nombreVacuna} ---> {nombreNew}
                  {dbEdit.cantidadRestante} ---> {cantidadNew}
                  Escribe CONFIRMAR en mayusculas para aplicar los cambios
                  """)
            confirm = str(input())
            if(confirm == "CONFIRMAR"):
                dbEdit.nombreVacuna = nombreNew
                dbEdit.cantidadRestante = cantidadNew
                dbEdit.save()
                input("Presiona enter para ir al inicio")
                main()
            else:
                input("Cambios no efectuados presiona enter para ir al inicio")
                main()
        else:
            input("Esta vacuna seleccionada no existe presiona enter para ir al inicio")
            main()
    elif(selector == 2):
        connection = sqlite3.connect("vacunacion.db") 
        cursor = connection.cursor()
        cursor.execute(f"SELECT id, nombreVacuna, cantidadRestante FROM Vacuna")
        mytable = from_db_cursor(cursor)
        print(mytable)
        id = funciones.verificarDatos("Introduce el ID de la vacuna a modificar: ", 1)
        
        for lista in db.Vacuna.select():
            if (int(lista.id) == int(id)):
                    find = 1
        
        if(find == 1):
            dbEdit = db.Vacuna.select().where(db.Vacuna.id == id).get()
            cantidadNew = funciones.verificarDatos("Cuantas vacunas llegaron?: ", 1)
            print(f"""
                  Los cambios son:
                  {dbEdit.cantidadRestante} ---> {dbEdit.cantidadRestante+cantidadNew}
                  Escribe CONFIRMAR en mayusculas para aplicar los cambios
                  """)
            confirm = str(input())
            if(confirm == "CONFIRMAR"):
                dbEdit.cantidadRestante = dbEdit.cantidadRestante+cantidadNew
                dbEdit.save()
            else:
                input("Cambios no efectuados presiona enter para ir al inicio: ")
                main()
        else:
            input("Esta vacuna seleccionada no existe presiona enter para ir al inicio")
            main()
    elif(selector == 3):
        datab = db.Vacuna()
        datab.nombreVacuna = funciones.verificarDatos("Introduce el nombre de la vacuna: ", 2)
        datab.cantidadRestante = funciones.verificarDatos("Introduce la cantidad de vacunas disponible: ", 1)
        datab.save()
        input("Vacuna agregada presiona enter para ir al inicio: ")
        main()
    
    elif(selector == 4):
        connection = sqlite3.connect("vacunacion.db") 
        cursor = connection.cursor()
        cursor.execute(f"SELECT id, nombreVacuna, cantidadRestante FROM Vacuna")
        mytable = from_db_cursor(cursor)
        print(mytable)
        id = funciones.verificarDatos("Introduce el ID de la vacuna a modificar: ", 1)
        
        for i in db.Vacuna.select():
            if (int(i.id) == int(id)):
                    find = 1
        if(find == 1):
            dbEdit = db.Vacuna.select().where(db.Vacuna.id == id).get()
            txt = str(dbEdit.nombreVacuna)
            texto = f"vas a elimininar {txt} estas seguro? Escribe CONFIRMAR en mayusculas si estas seguro: "
            selecto = funciones.verificarDatos(texto, 2)
            if(selecto == "CONFIRMAR"):
                dbEdit.delete_instance()
            else:
                input("Cambios no efectuados presiona enter para ir al inicio")
                main()
        else:
            input("Tu seleccion no existe presiona enter para ir al inicio")
            main()
    else:
        input("Tu seleccion no existe presiona enter para ir al inicio")
        main()   