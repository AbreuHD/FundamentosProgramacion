from geopy.geocoders import Nominatim
from peewee import *
from prettytable import from_db_cursor
import sqlite3
import os
import folium
from geopy.geocoders import Nominatim
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
    elif (selector == 3):
            dato1 = input(dato)
            if(len(dato1) > 0):
                return dato1
            else:
                print("Introduce algo, presiona enter para volver a intentar")
                verificarDatos(dato, selector)
    
def verUsuarios(main, arg = 0):
    os.system('cls')
    connection = sqlite3.connect("motores.db") 
    cursor = connection.cursor()
    cursor.execute("SELECT id,  nombre, cedula, telefono, direccion, act FROM User")
    mytable = from_db_cursor(cursor)
    print(mytable)
    if (arg == 1):
        return
    else:
        input("Presiona enter para ir al inicio")
        os.system('cls')
        main()
def verMotos(main, arg = 0):
    os.system('cls')
    connection = sqlite3.connect("motores.db") 
    cursor = connection.cursor()
    cursor.execute("SELECT id,  marca, modelo, placa, chasis, lat, lng, descripcion FROM Motos")
    mytable = from_db_cursor(cursor)
    print(mytable)
    if (arg == 1):
        return

def Agregar(main, dataB):
    db = dataB.User()
    cedula = verificarDatos("Introduce tu cedula: ", 1)
    try:
        searchP = dataB.User.select().where(dataB.User.cedula == cedula).get()
        exist = verificarDatos("Tu cedula ya existe en la base de datos, persiona 1 para ir al inicio o 2 para agregarle una moto: ", 1)
        if(exist == 1):
            main()
        elif(exist == 2):
            AgregarMoto(main, dataB, searchP)
    except:
        db.cedula = cedula
        db.nombre = verificarDatos("Introduce tu nombre: ", 2)
        db.telefono = verificarDatos("Introduce tu telefono sin guiones: ", 1)
        db.direccion = verificarDatos("Introduce tu direccion: ", 3)
        db.act = verificarDatos("Introduce que haces con el motor: ", 3)
        db.save()
    tabla = dataB.User.select().where(dataB.User.cedula == cedula).get()
    input("Tu info a sido guardada con exito, presiona enter para agregar la info de tu motor ")
    AgregarMoto(main, dataB, tabla)

def VerificarDireccion(dab):
    geolocator = Nominatim(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
    latitud = float(input("Introduce la latitud: "))
    longitud = float(input("Introduce la longitud: "))
    location = geolocator.reverse(f"{latitud}, {longitud}")
    if(str(location).find("República Dominicana") > 0):
        dab.lat = latitud
        dab.lng = longitud
        return
    else:
        input(f"Debes ingresar una langitud y longitud que corresponda a RD y no a {location}")
        return VerificarDireccion(dab)

def AgregarMoto(main, dataB, tabla):
    dab = dataB.Motos()
    dab.idUser = tabla.id
    dab.marca = verificarDatos("Introduce la marca de tu motor: ", 3)
    dab.modelo = verificarDatos("Introduce el modelo de tu motor: ", 3)
    dab.placa = verificarDatos("Introduce la placa de tu motor: ", 3)
    dab.chasis = verificarDatos("Introduce tu chasis: ", 3)
    VerificarDireccion(dab)
    dab.descripcion = verificarDatos("Introdice una descripcion sobre el motor: ", 3)
    dab.save()
    input("Presiona enter para ir al inicio")
    os.system('cls')
    main()

def Eliminar(main, dataB):
    selector = verificarDatos("Presiona 1 si quieres eliminar una persona o 2 si quieres eliminar una moto: ", 1)
    find = 0
    if(selector == 1):
        verUsuarios(main, 1)
        selec = verificarDatos("Selecciona el id a eliminar: ", 1)
        for lista in dataB.User.select():
            if(lista.id == selec):
                find = 1
        if(find != 1):
            input("Has seleccionado un dato inexistente presiona enter para ir al inicio ")
            main()
        tabla = dataB.User.select().where(dataB.User.id == selec).get()
        print(f" has seleccionado {tabla.nombre} ~ {tabla.nombre}")
        confirm = verificarDatos("Estas seguro? si eliminas la persona si moto tambien sera eliminada, Escribe CONFIRMAR en mayuscula para confirmar: ", 2)
        if(confirm == "CONFIRMAR"):
            try:
                motor = dataB.Motos.select().where(dataB.Motos.id == selec).get()
                motor.delete_instance()
            except:
                print("Esta persona no tenia Motores")
            tabla.delete_instance()
            input("Cambios efectuados, presiona enter para ir al inicio")
            os.system('cls')
            main()
        else:
            input("Has seleccionado un dato inexistente presiona enter para ir al inicio ")
            main()
    elif(selector == 2):
        verMotos(main, 1)
        selec = verificarDatos("Selecciona el id a eliminar: ", 1)
        for lista in dataB.Motos.select():
            if(lista.id == selec):
                find = 1
        if(find != 1):
            input("Has seleccionado un dato inexistente presiona enter para ir al inicio ")
            main()
        tabla = dataB.Motos.select().where(dataB.Motos.id == selec).get()
        print(f" has seleccionado {tabla.marca} ~ {tabla.modelo}")
        confirm = verificarDatos("Estas seguro? Escribe CONFIRMAR en mayuscula para confirmar: ", 2)
        if(confirm == "CONFIRMAR"):
            tabla.delete_instance()
            input("Tus cambios han sido efectuados, presiona enter para ir al inicio")
            os.system('cls')
            main()
        else:
            input("Has seleccionado un dato inexistente presiona enter para ir al inicio ")
            main()
    else: 
        input("Has seleccionado un dato inexistente presiona enter para ir al inicio ")
        main()

def Exportar(main, dataB):
    m = folium.Map(location=[18.9830219, -70.9375461], zoom_start=8.34)
    tooltip = "Clickea para ver la info"
    for lista in dataB.User.select():
        try:
            tabla = dataB.Motos.select().where(dataB.Motos.idUser_id == lista.id).get()
            folium.Marker(
                location=[tabla.lat, tabla.lng],
                popup= folium.Popup(f"<center><b>Motor marca {tabla.marca} de {lista.nombre}</b> <br> <i>modelo {tabla.modelo} y su placa {tabla.placa}</i></center>", max_width=300,min_width=300),
                icon=folium.Icon(color="green"),
                ).add_to(m)
        except:
            print(f"{lista.nombre} no tiene una moto")
    nameFila = verificarDatos("Introduce el nombre del archivo: ", 2)
    m.save(nameFila+'.html')
    webbrowser.open_new_tab(nameFila+'.html')
    input("Presiona enter para ir al inicio")
    os.system('cls')
    main()

def ExportarLicencia(main, dataB):
    find = 0
    verMotos(main, 1)
    selec = verificarDatos("Selecciona el id: ", 1)
    for lista in dataB.Motos.select():
        if(lista.id == selec):
            find = 1
    if(find != 1):
        input("Has seleccionado un dato inexistente presiona enter para ir al inicio ")
        main()
    try:
        tabla = dataB.Motos.select().where(dataB.Motos.id == selec).get()
        print(f" has seleccionado {tabla.marca} ~ {tabla.modelo} ~ {tabla.placa}")
        persona = dataB.User.select().where(dataB.User.id == tabla.idUser_id).get()
    except:
        input("Esta id no exite o no tiene asignado un motor, presiona enter para ir al inicio")
        main()
        
    nameFile = verificarDatos("Introduce el nombre del archivo: ", 2)
    file = open(nameFile+'.html','x', encoding='utf-8')
    file.write(f"""
        <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cedula</title>
    </head>
    <body style="background:url(https://static9.depositphotos.com/1113140/1105/i/600/depositphotos_11058932-stock-photo-white-wood-background.jpg)">
            </div> 
            <div style="margin-left:auto; margin-right:auto; border-radius: 25px; border:2px solid #ffffff; width: 700px; background:linear-gradient(-30deg, rgb(146,216,33), rgb(255,255,255))">
                <h2 style="text-align: center;">Nombre: {persona.nombre}</h2>
                <h2 style="text-align: center;">Cedula: {persona.cedula}</h2>                
                <h3 style="text-align: center;">Telefono: {persona.telefono}</h3>
                <h3 style="text-align: center;">Direccion: {persona.direccion}</h3>
                <h3 style="text-align: center;">Actividad: {persona.act}</h3>
                <h3 style="text-align: center;">Marca: {tabla.marca}</h3>
                <h3 style="text-align: center;">Modelo: {tabla.modelo}</h3>
                <h3 style="text-align: center;">Placa: {tabla.placa}</h3>
                <h3 style="text-align: center;">Chasis: {tabla.chasis}</h3>
                <h3 style="text-align: center;">Latitud y Longititud: {tabla.lat} {tabla.lng}</h3>
                <h3 style="text-align: center;">Descripcion: {tabla.descripcion}</h3>
            </div>
    </body>
    </html>
    """)
    file.close
    webbrowser.open_new_tab(nameFile+'.html')