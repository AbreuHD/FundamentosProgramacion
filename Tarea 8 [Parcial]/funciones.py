from peewee import *
import datab
from geopy.geocoders import Nominatim
import sqlite3
from prettytable import from_db_cursor
import folium
import webbrowser

def vericarDatos(dato, selecto = 0):
    if(selecto == 0):
        info = input(dato)
        if(len(info) == 0):
            print("Debes introducir algun caracter")
            return vericarDatos(dato)
    elif (selecto == 1):
        try:
            info = float(input(dato))
        except:
            print("Este campo no se puede dejar vacio y no soporta caracteres de texto")
            return  vericarDatos(dato, 1)
    elif (selecto == 2):
        info = str(input(dato))
        for txt in info:
            for a in range(0,10):
                if(str(txt).find(str(a)) > 0):
                    return vericarDatos(dato, 2)
    return info

def ver(main,select = 0):
    connection = sqlite3.connect("Robos.db")
    cursor = connection.cursor()
    cursor.execute("SELECT cedula, fecha, objetoRobado, valor, lugar, lat, lng FROM Robo")
    mytable = from_db_cursor(cursor)
    print(mytable)
    if(select == 0):
        return
    else:
        sel = vericarDatos("Presiona 1 si quieres ir al menu o 2 si quieres agregar un robo: ", 1)
        if(sel == 1): main()
        elif(sel == 2): agregar(main)
        else:
            input("Debes introducir un numero de los que dice arriba, presiona enter para ir al inicio")
            main()
def agregar(main):
    data = datab.Robo()
    data.cedula = vericarDatos("Introduce la cedula de la persona: ", 1)
    data.nombre = vericarDatos("Introduce el nombre de la persona: ", 2)
    data.fecha = vericarDatos("Introduce la fecha del robo: ")
    data.objetoRobado = vericarDatos("Introduce el nombre del objeto robado: ", 2)
    data.valor = vericarDatos("Introduce el valor del objeto robado: ", 1)
    lugar(data)
    data.save()
    sel = vericarDatos("Presiona 1 si quieres ir al menu o 2 si quieres agregar un robo: ", 1)
    if (sel == 1):
        main()
    elif (sel == 2):
        agregar(main)
    else:
        input("Debes introducir un numero de los que dice arriba, presiona enter para ir al inicio")
        main()

def lugar(data):
    lat = vericarDatos("Introduce la latitud: ", 1)
    lng = vericarDatos("Introduce la longitud: ", 1)
    geo = Nominatim(user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41")
    coordenadas = f"{lat},{lng}"
    locacion = geo.reverse(coordenadas)
    if(str(locacion).find("República Dominicana") > 0):
        data.lat = lat
        data.lng = lng
        data.lugar = locacion
    else:
        print("Debes agregar una latitud y longitud que sean de Republica Dominicana")
        return lugar(data)
    return

def editar(main):
    ver(main)
    find = 0
    seleccion = vericarDatos("Introduce la cedula de la persona que quieres modificar", 1)
    for a in datab.Robo.select():
        if (a.cedula == seleccion):
            find = 1
    if (find == 0):
        input("Esta cedula no existe presiona enter para ir al inicio: ")
        main()
    data = datab.Robo.select().where(datab.Robo.cedula == seleccion).get()
    cedulaN = vericarDatos("Introduce la nueva cedula: ", 1)
    nombreN = vericarDatos("Introduce el nuevo nombre: ", 2)
    fechaN = vericarDatos("Introduce la nueva fecha: ")
    objetoN = vericarDatos("Introduce el nuevo objeto: ", 2)
    valorN = vericarDatos("Introduce el nuevo valor: ", 1)
    lat = data.lat
    lng = data.lng
    lugar(data)
    print(f"""
    Estas seguro de que quieres efectuar estos cambios?
    
    {data.cedula} ----> {cedulaN}
    {data.nombre} ----> {nombreN}
    {data.fecha} ----> {fechaN}
    {data.objetoRobado} ----> {objetoN}
    {data.valor} ----> {valorN}
    {lat} ----> {data.lat}
    {lng} ----> {data.lng}

    Si estas seguro del cambio escribe CONFIRMAR todo en mayusculas
    """)
    confirm = vericarDatos(": ", 2)
    if(confirm == "CONFIRMAR"):
        data.cedula = cedulaN
        data.nombre = nombreN
        data.fecha = fechaN
        data.objetoRobado = objetoN
        data.valor = valorN
        data.save()
        sel = vericarDatos("Presiona 1 si quieres ir al menu o 2 si quieres agregar un robo: ", 1)
        if(sel == 1): main()
        elif(sel == 2): agregar()
        else:
            input("Debes introducir un numero de los que dice arriba, presiona enter para ir al inicio")
            main()
    else:
        input("Modificacion cancelada presiona enter para ir al inicio ")
        main()

def exportar(main):
    m = folium.Map(location=[18.833409,-70.4097728], zoom_start=8.98)
    tooltip = "Click para ver mas"
    for lista in datab.Robo.select():
        folium.Marker(
            location=[lista.lat,lista.lng],
            popup=folium.Popup(
                f"<center><b>Cedula {lista.cedula} de {lista.nombre}</b> <br> <i> fecha del robo {lista.fecha} objeto robado {lista.objetoRobado} con un valor de {lista.valor} <br> lugar del robo: {lista.lugar} <br> coordenadas {lista.lat} {lista.lng}</i></center>",
                max_width=300, min_width=300),
            icon = folium.Icon(color="green")
        ).add_to(m)
    nameFile = vericarDatos("Introduce el nombre del mapa", 2)
    m.save(nameFile+".html")
    webbrowser.open_new_tab(nameFile+".html")
    sel = vericarDatos("Presiona 1 si quieres ir al menu o 2 si quieres agregar un robo: ", 1)
    if (sel == 1):
        main()
    elif (sel == 2):
        agregar(main)
    else:
        input("Debes introducir un numero de los que dice arriba, presiona enter para ir al inicio")
        main()