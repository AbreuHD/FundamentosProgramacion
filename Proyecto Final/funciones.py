import sqlite3
from prettytable import from_db_cursor
import db
import datetime
from geopy.geocoders import Nominatim
import random


def verificarDato(info, select = 0, datab = "", d = 0, fecha = 0):
    dato = ''
    if (select == 0):
        try:
            dato = float(input(info))        
        except:
            print('Recuerda que este campo no puede estar vacio y solo acepta numeros.')
            verificarDato(info)

    elif (select == 1):
        dato = str(input(info))
        if (len(dato) == 0):
            print("Este campo no puede estar vacio")
            verificarDato(info, 1)
            
        for a in dato:
            for b in range(0,10):
                if (a == b):
                    print("Recuerda que este campo no acepta numeros")
                    verificarDato(info, 1)
    
    elif (select == 2):
        dato = input(info)
        if (len(dato) == 0):
            print("Este campo no puede estar vacio")
            verificarDato(info, 2, 0, 0, 1)
        if (fecha == 1):
            if(str(dato).find('.') < 0):
                print("Debes introducir un link valido")
                verificarDato(info, 2, 0, 0, 1)
    
    elif (select == 3):
        dato = str(input(info))
        if (dato.lower() == "f" or dato.lower() == "m"):
            pass
        else:
            if (d == 1 and dato == "0"):
                pass
            else:
                print("Solo se acepta F o M")
                verificarDato(info, 3)
    
    elif (select == 4):
        dato = int(input(info))
                    
        if (dato == 1):
            datab.estado = "Vivo"
        elif (dato == 2):
            datab.estado = "Muerto"
        elif (dato == 3):
            datab.estado = "Indefinido"
        else:
            if(d != 0 and dato == 0):
                pass
            else:
                print("debes seleccionar un estado de los que estan en la lista")
                verificarDato(4)
        return datab.estado   
    elif (select == 5):
        try:
            lat = input("Introduce la latitud donde esta el personaje, si esta fuera de la tierra pon una x : ")
            if(lat.lower() == 'x'):
                rnd = ((random.randint(0,99)/100)/100)/100
                datab.lat = 18.08739+rnd
                datab.lng = -71.45291
                datab.direccion = verificarDato("En que planeta se encuentra el personaje? ", 1)
                return
            lng = input("Introduce la longitud donde esta el personaje: ")
            if(lat == 0 and d != 0):
                pass
            else:
                datab.lat = lat
            if(lng == 0 and d != 0):
                pass
            else:   
                datab.lng = lng
            
            if (len(str(datab.lat)) > 0 and len(str(datab.lng)) > 0):
                geolocator = Nominatim(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
                datab.direccion= geolocator.reverse(f"{str(datab.lat)}, {str(datab.lng)}")
            else:
                direccion = verificarDato("Donde se encuentra el personaje? ", 2)
                if (direccion == 0 and d != 0):
                    pass
                else:
                    datab.direccion = direccion     
    
        except:
            print("Debes introducir valores validos")
            verificarDato(info,5,datab)
        return
        
    elif (select == 6):
        try:
            dato = int(input(info))
            if(fecha == 'd' and dato > 31 or dato < 1 and fecha == 'd'):
                print("debe introducir un numero valido")
                verificarDato(info, 6)
            elif (fecha == 'm' and dato > 12 or fecha == 'm' and dato < 1):
                print("debe introducir un numero valido")
                verificarDato(info, 6)
            elif (fecha == 'a' and dato < 1):
                print("debe introducir un numero valido")
                verificarDato(info, 6)
                
        except:
            print("Solo se aceptan numeros")
            verificarDato(info, 6)        
    return dato

def fecha(datab, d = 0):
    signo = ""
    hoy = datetime.date.today()
    dia = verificarDato("Introduce el dia que nacio el personaje: ", 6, 0, 0, 'd')
    mes = verificarDato("Introduce el mes que nacio el personaje: ", 6, 0, 0, 'm') 
    age = verificarDato("Introduce el año que nacio el personaje: ", 6, 0, 0, 'a')
    if (dia == 29 and mes == 2 and age % 4 != 0 and age % 100 != 0 and age % 400 != 0):
        print("introduzca un dia valido")
        fecha(datab, d)
    elif (dia == 29 and age % 4 != 0):
        print("introduzca un dia valido")
        fecha(datab, d)
    elif (dia > 29 and mes == 2):
        print("introduzca un dia valido")
        fecha(datab, d)
    elif (dia > 30 and mes == 4):
        print("introduzca un dia valido")
        fecha(datab, d)
    elif (dia > 30 and mes == 6):
        print("introduzca un dia valido")
        fecha(datab, d)
    elif (dia > 30 and mes == 9):
        print("introduzca un dia valido")
        fecha(datab, d)
    elif (dia > 30 and mes == 11):
        print("introduzca un dia valido")
        fecha(datab, d)
    edad = hoy.year - age
    
    fechaNacimiento = str(dia) + "-" + str(mes) + "-" + str(age)
    if(dia <= 0 and d == 0 or mes <= 0 and d == 0 or age <= 0 and d == 0):
        print("debes introducir una fecha valida: ")
        fecha(datab)
    if(fechaNacimiento != "0-0-0"):
        signosZ =   [['Acuario', 1, 20], 
                    ['Piscis', 2, 19], 
                    ['Aries', 3, 21], 
                    ['Tauro', 4, 20], 
                    ['Geminis', 5, 21], 
                    ['Cancer', 6, 21], 
                    ['Leo', 7, 23], 
                    ['Virgo', 8, 23], 
                    ['Libra', 9, 23], 
                    ['Escorpio', 10, 23], 
                    ['Sagitario', 11, 22],
                    ['Capricornio', 12, 22]]
        if(fechaNacimiento == "0-0-0"): fechaNacimiento = datab.nacimiento
        for i in range(len(signosZ)):
            if(mes == signosZ[i][1]):
                if(int(dia) < signosZ[i][2]):
                    signo = signosZ[i-1][0]
                else: signo = signosZ[i][0]
    
        if (mes < int(hoy.strftime("%m"))):
            edad = edad
        elif (dia <= int(hoy.strftime("%d")) and mes == int(hoy.strftime("%m"))):
            edad = edad
        else: edad = edad-1
        print(signo)
        datab.zodiaco = signo
        datab.edad = edad
    
    return fechaNacimiento

def gestion(main, select, ids= 0):
    if (select == 1):
        animeN = ''
        datab = db.Personajes()
        verDatos(0)
        
        anime = verificarDato("El anime al cual pertenece el anime existe el los datos de arriba?, presiona 1 si existe o 2 para agregar el anime: ")
        if (anime == 1):
            anime = verificarDato("Selecciona el id del anime al cual el personaje pertenece: ")
            for a in db.Animes.select():
                if a.id == anime:
                    animeN = a.nombreAnime
            if (len(animeN) == 0):
                input("Este anime no existe en la lista de arriba, presiona enter para ir al inicio")
                main()
        
            datab.nombre = verificarDato("Introduce el nombre del personaje: ", 1)
            datab.apellido = verificarDato("Introduce el apellido del personaje: ", 1)
            for a in db.Personajes.select():
                if (str(a.nombre).lower() == str(datab.nombre).lower() and str(a.apellido).lower() == str(datab.apellido).lower()):
                    similar = verificarDato("Este personaje es similar a este, presiona  1 si son diferentes, 2 para modificar el personaje o 3 para ir al inicio")
                    if (similar == 1):
                        pass
                    elif (similar == 2):
                        gestion(main,2,a.id)
                    elif (similar == 3):
                        input("Presiona enter para continuar")
                        main()
                    else:
                        input("seleccion incorrecta, presiona enter para ir al inicio")
                        main()
            datab.foto = verificarDato("Introduce el link de tu imagen: ", 2, 0, 0, 1)
            datab.pronunciacion = verificarDato("Introduce como se pronuncia dicho nombre: ", 2)
            datab.serie = animeN
            datab.nacimiento = fecha(datab)
            datab.poder = verificarDato("Introduce el nombre del poder del personaje: ", 2)
            datab.fraseFav = verificarDato("Introduce la frase favorita del personaje: ", 2)
            datab.descripcionR = verificarDato("Describe la ropa del personaje: ", 2)
            datab.altura = verificarDato("Cual es la altura en CM del personaje: ")
            datab.sexo = verificarDato("Cual es el genero del personaje? introduce F o M: ", 3)
            datab.estado = verificarDato("Como esta el personaje? 1 = vivo, 2 = muerto o 3 = indefinido: ", 4, datab)
            verificarDato("lat", 5, datab)
            listA = db.Animes.select().where(db.Animes.id == anime).get()
            listA.cantidadPersonaje = int(listA.cantidadPersonaje) +1
            listA.save()
            datab.save()
                        
        elif (anime == 2):
            input("Presiona enter para ir a agregar el anime")
            config(main, 1, 1)
        else:
            input("Debes seleccionar 1 o 2, presiona enter para ir al inicio")
            main()
            
    elif (select == 2):
        verDatos(1)
        if(ids == 0):
            personajeid = verificarDato("Escribe el id del personaje que deseas modificar: ")
        else:
            personajeid = ids
        for a in db.Personajes.select():
            if (a.id == personajeid):
                personaje = a.nombre
        if(len(personaje) == 0):
            input("Este id no existe, presiona enter para ir al inicio")
            main()
            
        lista = db.Personajes.select().where(db.Personajes.id == personajeid).get()

        print("Seleccionaste", personaje, "Escribe lo que quieras que diga ahora, pon 0 si quieres dejar los mismos datos")
        nombre = verificarDato("Introduce el nuevo nombre: ", 1)
        apellido = verificarDato("Introduce el nuevo apellido: ", 1)
        foto = verificarDato("Introduce la nueva foto: ",  2, 0, 0, 1)
        pronunciacion = verificarDato("Introduce la nueva pronunciacion: ", 2)
        verDatos(0)
        anime = verificarDato("Introduce el id del anime el cual pertenece el personaje: ")
        if (anime != 0):
            for a in db.Animes.select():
                if a.id == anime:
                    anime = a.nombreAnime
            if (len(anime) == 0):
                input("Este anime no existe en la lista de arriba, presiona enter para ir al inicio")
                main()
                
        fechaN = fecha(lista, 1)
        poder = verificarDato("Introduce el nuevo poder: ", 2)
        frasef = verificarDato("Introduce la frase favorita: ", 2)
        descripcion = verificarDato("Introduce la nueva descripcion: ", 1)
        altura = verificarDato("Introduce la nueva altura en CM: ")
        sexo = verificarDato("Introduce el nuevo sexo, F o M : ", 3, 0, 1)
        estado = verificarDato("Introduce el nuevo estado: ", 4, lista, 1)
        verificarDato("lat", 5, lista)
        if (nombre == "0"): nombre = lista.nombre
        if (apellido == "0"): apellido = lista.apellido
        if (foto == "0"): foto = lista.foto
        if (pronunciacion == "0"): pronunciacion = lista.pronunciacion
        if (anime == 0): anime = lista.serie
        if (poder == "0"): poder = lista.poder
        if (frasef == "0"): frasef = lista.fraseFav
        if (descripcion == "0"): descripcion = lista.descripcionR
        if (altura == 0): altura = lista.altura
        if (sexo == "0"): sexo = lista.sexo
        if (estado == "0"): estado = lista.estado

        print(f"""
                           CAMBIOS
            {lista.nombre} -----------> {nombre}              
            {lista.apellido} -----------> {apellido}              
            {lista.foto} -----------> {foto}              
            {lista.pronunciacion} -----------> {pronunciacion}              
            {lista.serie} -----------> {anime}  
            {lista.nacimiento} -----------> {fechaN}                          
            {lista.poder} -----------> {poder}              
            {lista.fraseFav} -----------> {frasef}              
            {lista.descripcionR} -----------> {descripcion}              
            {lista.altura} -----------> {altura}              
            {lista.sexo} -----------> {sexo}              
            {lista.estado} -----------> {estado}          
        Escribe CONFIRMAR en mayusculas para confirmar la modificacion
              """)
        
        mod = verificarDato(": ", 1)
        if (mod == "CONFIRMAR"):
            lista.save()
        else:
            input("Cambios cancelados, presiona enter para ir al incio ")
            main()
            
    elif (select == 3):
        verDatos(1)
        find = ""
        selecto = verificarDato("Introduce el id del personaje que deseas eliminar: ")
        for a in db.Personajes.select():
            if (selecto == a.id):
                find = a.nombre
                
        if (len(find) == 0):
            input("Este id no existe, presiona enter para ir al inicio")
            main()
        tabla = db.Personajes.select().where(db.Personajes.id == selecto).get()
        print(f"Acabas de seleccionar {find}, estas seguro que deseas eliminarlo? Escribe CONFIRMAR, en mayusculas si quieres eliminar el dato")
        conf = verificarDato(": ", 1)
        if(conf == "CONFIRMAR"):
            listA = db.Animes.select().where(db.Animes.nombreAnime == tabla.serie).get()
            listA.cantidadPersonaje = int(listA.cantidadPersonaje) -1
            listA.save()
            tabla.delete_instance()
        else:
            input("Eliminacion Cancelada, presiona enter para ir al inicio")
            main()
    input("Presiona enter para ir al inicio")
    main()
def reportes(main, select):
    if (select == 1):
        verDatos(1)

    elif (select == 2):
        zodiaco = [[0, "Acuario"],
                   [0, "Piscis"],
                   [0, "Aries"],
                   [0, "Tauro"],
                   [0, "Geminis"],
                   [0, "Cancer"],
                   [0, "Leo"],
                   [0, "Virgo"],
                   [0, "Libra"],
                   [0, "Escorpio"],
                   [0, "Sagitario"],
                   [0, "Capricornio"]]
        for a in db.Personajes.select():
            for b in range(len(zodiaco)):
                if (a.zodiaco == zodiaco[b][1]):
                    zodiaco[b][0] += 1
        for a in range(len(zodiaco)):
            if (zodiaco[a][0] != 0):
                print(f"{zodiaco[a][1]} tiene : {zodiaco[a][0]} personajes")
        print("")
        for a in db.Personajes.select().order_by(db.Personajes.zodiaco):
            print (f"{a.zodiaco}, {a.nombre}, {a.apellido}, {a.serie}, {a.sexo}")
    
    elif (select == 3):
        verDatos(0)
            
    elif (select == 4):
        estados = [[0,"Vivo"],
                   [0, "Muerto"],
                   [0, "Indefinido"]]
        for a in db.Personajes.select():
            for b in range(len(estados)):
                if (a.estado == estados[b][1]):
                    estados[b][0] += 1
        for a in range(len(estados)):
            if (estados[a][0] != 0):
                print(f"{estados[a][1]} tiene : {estados[a][0]} personajes")
        print("")
        for a in db.Personajes.select().order_by(db.Personajes.estado):
            print (f"{a.estado}, {a.nombre}, {a.apellido}, {a.serie}, {a.sexo}")
    input("Presiona enter para ir al inicio")
    main()

def config(main, selecto, sel = 0):
    if (selecto == 1):
        anime = db.Animes()
        anime.nombreAnime = verificarDato("Introduce el nombre del anime: ", 1)
        for a in db.Animes.select():
            if (a.nombreAnime == anime.nombreAnime):
                mod = verificarDato("hay un anime llamado asi en la base de datos, pulsa enter para ir al inicio")
                main()
        anime.cantidadPersonaje = 0
        anime.save()
        if(sel == 1): 
            gestion(main,1)
    elif (selecto == 2):
        verDatos(0)
        find = ""
        selecto = verificarDato("Introduce el id del anime el cual deseas modificar: ")
        for a in db.Animes.select():
            if (selecto == a.id):
                print("A")
                find = a.nombreAnime
        if (len(find) == 0):
            print(find)
            input("Este id no existe, presiona enter para ir al inicio")
            main()
        dataS = db.Animes.select().where(db.Animes.id == selecto).get()
        newN = verificarDato("Introduce el nuevo nombre del anime: ", 1)
        print(f"""
                            CAMBIOS
                {dataS.nombreAnime} ------------> {newN}            
              Escribe CONFIRMAR, en mayusculas para confirmar el cambio
              """)
        confirm = verificarDato(": ", 1)
        if (confirm == "CONFIRMAR"):
            for a in db.Personajes.select():
                if (a.serie == str(dataS.nombreAnime)):
                    serieN = db.Personajes.select().where(db.Personajes.id == a.id).get()
                    serieN.serie = newN
                    serieN.save()
            dataS.nombreAnime = newN
            dataS.save()
        else:
            input("Cambios cancelados, presiona enter para ir al inicio")
            main()
    elif (selecto == 3):
        find = ""
        verDatos(0)
        selecto = verificarDato("Introduce el id del anime que desea eliminar, recuerda que si borras un anime borraras todos los personajes que estan en el: ")
        for a in db.Animes.select():
            if (selecto == a.id):
                find = a.nombreAnime
        if (len(find) == 0):
            input("Este id no existe, presiona enter para ir al inicio")
            main()
        info = f"A seleccionado eliminar {find}, escriba CONFIRMAR todo en mayusculas si quiere hacerlo, recuerda que todos los personajes en el tambien se eliminaran: "
        confirm = verificarDato(info, 1)
        if (confirm == "CONFIRMAR"):
            lista = db.Animes.select().where(db.Animes.id == selecto).get()
            for a in db.Personajes.select():
                try:
                    if (a.serie == lista.nombreAnime):
                            animedel = db.Personajes.select().where(db.Personajes.id == a.id).get()
                            animedel.delete_instance()
                except:
                    pass
            lista.delete_instance()
        else: 
            input("Eliminado cancelado, presiona enter para ir al inicio")
            main()
    elif (selecto ==  4):
        sexo = [[0,"F"],
                [0, "M"]]
        for a in db.Personajes.select():
            for b in range(len(sexo)):
                if (a.sexo == sexo[b][1]):
                    sexo[b][0] += 1
        for a in range(len(sexo)):
            if (sexo[a][0] != 0):
                print(f"{sexo[a][1]} tiene : {sexo[a][0]} personajes")
        print("")
        for a in db.Personajes.select().order_by(db.Personajes.sexo):
            print (f"{a.sexo}, {a.nombre}, {a.apellido}, {a.serie}")
    input("Presiona enter para ir al inicio")
    main()

def verDatos (select):
    connection = sqlite3.connect("AnimeData.db")
    cursor = connection.cursor()
    if (select == 0):
        cursor.execute("SELECT id, nombreAnime, cantidadPersonaje FROM Animes")
        mytable = from_db_cursor(cursor)
        print(mytable)    

    elif (select == 1):
        cursor.execute("SELECT id, nombre, apellido, serie, sexo, edad FROM Personajes")
        mytable = from_db_cursor(cursor)
        print(mytable)    
    return