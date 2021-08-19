import db
import funciones
import os
import webbrowser
import folium


def main():
    os.system('cls')
    print("""
            ╔═════════════════════════════════════════════════════════════════════════════╗
            ║                                                                             ║
            ║                    ███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗                    ║
            ║                    ████╗░████║██╔════╝████╗░██║██║░░░██║                    ║
            ║                    ██╔████╔██║█████╗░░██╔██╗██║██║░░░██║                    ║
            ║                    ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║                    ║
            ║                    ██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝                    ║
            ║                    ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░                    ║
            ║≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈║
            ║               Introduce un numero para hacer dicha accion.                  ║
            ║                                                                             ║
            ║                                1 = Gestionar Personajes                     ║
            ║                                2 = Reportes                                 ║
            ║                                3 = Configuracion                            ║
            ║                                4 = Acerca de                                ║
            ║                                0 = Salir                                    ║  
            ║                                                                             ║
            ╚═════════════════════════════════════════════════════════════════════════════╝ 
           """)
    selecto = funciones.verificarDato(': ')
    if (selecto == 1):
            gestionA()
    elif (selecto == 2):
            reportesA()
    elif (selecto == 3):
            configA()
    elif (selecto == 4):
            about()
    elif (selecto == 0):
          pass
    else:
          print("Debes introducir un numero valido")
          main()


def gestionA():
      os.system('cls')
      print("""
            ╔═════════════════════════════════════════════════════════════════════════════╗
            ║                                                                             ║
            ║                             GESTIONAR PERSONAJES                            ║       
            ║                                                                             ║       
            ║               Introduce un numero para hacer dicha accion.                  ║
            ║                                                                             ║
            ║                                2 = Agregar                                  ║
            ║                                3 = Modificar                                ║
            ║                                4 = Eliminar                                 ║
            ║                                1 = Ir al inicio                             ║
            ║                                0 = Salir                                    ║
            ║                                                                             ║
            ║                                                                             ║
            ╚═════════════════════════════════════════════════════════════════════════════╝ 
          """)
      selecto =  funciones.verificarDato(': ')
      if (selecto == 2):
            funciones.gestion(main, 1)
      elif (selecto == 3):
            funciones.gestion(main, 2)
      elif (selecto == 4):
            funciones.gestion(main, 3)
      elif (selecto == 1):
            main()
      elif (selecto == 0):
            pass
      else:
            input("Debes introducir un dato valido, presiona enter para ir al incio")
            main()
            
def reportesA():
      os.system('cls')
      print("""
            ╔═════════════════════════════════════════════════════════════════════════════╗
            ║                                                                             ║       
            ║                                  REPORTES                                   ║
            ║                                                                             ║       
            ║               Introduce un numero para hacer dicha accion.                  ║
            ║                                                                             ║
            ║                            2 = Listado de personajes                        ║
            ║                            3 = Lista de personajes por zodiaco              ║
            ║                            4 = Mapa                                         ║
            ║                            5 = Exportar personaje                           ║
            ║                            6 = Lista de Animes                              ║
            ║                            7 = Personajes por estado                        ║
            ║                            1 = Ir al inicio                                 ║
            ║                            0 = Salir                                        ║
            ║                                                                             ║
            ║                                                                             ║
            ╚═════════════════════════════════════════════════════════════════════════════╝ 
          """)
      selecto = funciones.verificarDato(": ")
      if (selecto == 1):
            main()
      elif (selecto == 0):
            pass
      elif (selecto == 2):
            funciones.reportes(main, 1)
      elif (selecto == 3):
            funciones.reportes(main, 2)
      elif (selecto == 4):
            mapa()
      elif (selecto == 5):
            exportar()
      elif (selecto == 6):
            funciones.reportes(main, 3)
      elif (selecto == 7):
            funciones.reportes(main, 4)
def configA(select = 0):
      if (select == 0):
            os.system('cls')    
            print("""
            ╔═════════════════════════════════════════════════════════════════════════════╗
            ║                                                                             ║
            ║                                   CONFIG                                    ║       
            ║                                                                             ║       
            ║               Introduce un numero para hacer dicha accion.                  ║
            ║                                                                             ║
            ║                            2 = Series                                       ║
            ║                            3 = Estados                                      ║
            ║                            4 = Sexos                                        ║
            ║                            1 = Ir al inicio                                 ║
            ║                            0 = Salir                                        ║
            ║                                                                             ║
            ║                                                                             ║
            ╚═════════════════════════════════════════════════════════════════════════════╝ 
          """)
            selecto = funciones.verificarDato(": ")
            if(selecto == 1):
                  main()
            elif (selecto == 2):
                  configA(1)
            elif (selecto == 3):
                  funciones.reportes(main, 4)
            elif (selecto == 4):
                  funciones.config(main, 4)
            elif (selecto == 0):
                  pass
                  

      elif (select == 1):
            os.system('cls')    
            print("""
            ╔═════════════════════════════════════════════════════════════════════════════╗
            ║                                                                             ║
            ║                               ANIME CONFIG                                  ║       
            ║                                                                             ║       
            ║               Introduce un numero para hacer dicha accion.                  ║
            ║                                                                             ║
            ║                            2 = Agregar                                      ║
            ║                            3 = Editar                                       ║
            ║                            4 = Eliminar                                     ║
            ║                            1 = Ir atras                                     ║
            ║                            0 = Salir                                        ║
            ║                                                                             ║
            ║                                                                             ║
            ╚═════════════════════════════════════════════════════════════════════════════╝ 
          """)
            selecto = funciones.verificarDato(": ")
            if (selecto == 1):
                  configA()
            elif (selecto == 2):
                  funciones.config(main, 1)
            elif (selecto == 3):
                  funciones.config(main, 2)
            elif (selecto == 4):
                  funciones.config(main, 3)
            elif (selecto == 0):
                  pass
            else:
                  input("debe introducir un dato valido, presiona enter para ir al inicio")
                  main()
def about():
      os.system('cls')
      webbrowser.open_new_tab('https://www.youtube.com/watch?v=xGU-JTRdBRI')
      input("Presiona enter para ir al inicio")
      main()

def mapa():
      start = db.Personajes.select().where(db.Personajes.id == 1).get()
      m = folium.Map(location=[start.lat,start.lng], zoom_start=4)
      tooltip = "Click para ver mas"
      for lista in db.Personajes.select():
        folium.Marker(
            location=[lista.lat,lista.lng],
            popup=folium.Popup(
                f"<center><b> {lista.nombre} {lista.apellido} del anime: {lista.serie} </b> <br> <i> fecha de nacimiento: {lista.nacimiento} estado: {lista.estado} poder: {lista.poder} <br> zodiaco: {lista.zodiaco} frase favorita: {lista.fraseFav} </i></center>",
                max_width=300, min_width=300),
            icon = folium.Icon(color="green")
        ).add_to(m)
      nameFile = funciones.verificarDato("Introduce el nombre del mapa: ", 1)
      m.save(nameFile+".html")
      webbrowser.open_new_tab(nameFile+".html")
      input("Presiona enter para ir al inicio")
      main()
def exportar():
      funciones.verDatos(1)
      name = ""
      selecto = funciones.verificarDato("Introduce el id del personaje que desea exportar: ")
      for a in db.Personajes.select():
            if (a.id == selecto):
                  name = a.nombre
      if (len(name) == 0):
            input("Introdujiste un id que no existe, presiona enter para ir al inicio")
            main()
      animeL = db.Personajes.select().where(db.Personajes.id == selecto).get()
      nameFile = funciones.verificarDato(f"seleccionaste {name} introduce el nombre con el cual se guardara el archivo: ",1)
      file = open(nameFile+".html", "x", encoding='utf-8')
      file.write(f"""
                 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>2021-0308</title>
</head>
<body>
    <div style="margin-left:auto; margin-right:auto; margin-top: 250px">
        <img style="float:left; margin-left:150px; margin-right:0px; max-width: 20%" src="{animeL.foto}" >
        <h2 style="margin-left: 30%; text-align: center">nombre: {animeL.nombre} {animeL.apellido}</h2>
        <h4 style="margin-left: 30%; text-align: center">sexo: {animeL.sexo}</h4>
        <h3 style="margin-left: 30%; text-align: center">pronunciacion: {animeL.pronunciacion}</h3>
        <h4 style="margin-left: 30%; text-align: center">anime: {animeL.serie}</h4>
        <h4 style="margin-left: 30%; text-align: center">estado: {animeL.estado}</h4>
        <h4 style="margin-left: 30%; text-align: center">fecha: {animeL.nacimiento}</h4>
        <h4 style="margin-left: 30%; text-align: center">poder: {animeL.poder}</h4>
        <h4 style="margin-left: 30%; text-align: center">frase favorita: {animeL.fraseFav}</h4>
        <h4 style="margin-left: 30%; text-align: center">descripcion ropa: {animeL.descripcionR}</h4>
        <h4 style="margin-left: 30%; text-align: center">altura: {animeL.altura}</h4>
        <h4 style="margin-left: 30%; text-align: center">zodiaco: {animeL.zodiaco}</h4>
        <h4 style="margin-left: 30%; text-align: center">edad: {animeL.edad}</h4>
        <h4 style="margin-left: 30%; text-align: center">domicilio: {animeL.direccion}</h4>
        <h4 style="margin-left: 30%; text-align: center">latitud y longitud: {animeL.lat} {animeL.lng}</h4>
    </div>
</body>
</html>      
                 """)
      file.close()
      webbrowser.open_new_tab(nameFile+".html")
      input("Presiona enter para ir al inicio")
      main()
main()