import requests
import json
import webbrowser

print("""
 ____    ___   ____   _          ___   _____   ___    ___
|___ \  / _ \ |___ \ / |        / _ \ |___ /  / _ \  ( _ ) 
  __) || | | |  __) || | _____ | | | |  |_ \ | | | | / _ \      
 / __/ | |_| | / __/ | ||_____|| |_| | ___) || |_| || (_) |
|_____| \___/ |_____||_|        \___/ |____/  \___/  \___/
""")

numeroDeUsuarios = int(input("Ingresa el numero de usuarios que desea generar: "))
nombreArchivo = str(input("Ingresa el nombre que tendra el archivo generado: "))
datos = requests.get(f"https://randomuser.me/api/?results={numeroDeUsuarios}").json()
titulo = ""
nombre = ""
apellido = ""
pais = ""
genero = ""
fecha = ""
foto = ""
mujeres = 0
hombres = 0

html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Info</title>
</head>
<body style="background: url(https://www.wallpaperflare.com/static/944/260/967/comic-art-your-name-kimi-no-na-wa-white-wallpaper.jpg) fixed no-repeat 0 0;">"""

file = open(nombreArchivo+".html", "x", encoding='utf-8')
file.write(html)

for preinfo in datos['results']:
      if(preinfo['gender'] == "female"):
            mujeres += 1
      else: 
        hombres += 1
file.write(f"""
        <div style="width: auto; margin:0 auto; border:1px solid rgb(0, 0, 0); background:linear-gradient(30deg, rgb(204, 100, 120),rgba(97, 160, 45, 0.74), rgb(1, 63, 247), rgb(218, 207, 207), rgb(233, 93, 233));">
        <h1 style="text-align:center;">Cantidad de genero</h1>
        <h3 style="text-align:center;">Hay un total de {mujeres} mujeres</h3>
        <h3 style="text-align:center;">Hay un total de {hombres} hombres</h3>        
    </div>""")
for info in datos['results']:
    titulo = "Titulo: " + info['name']['title']
    nombre ="Nombre: " + info['name']['first']
    foto = info['picture']['large']
    apellido = "Apellido: " + info['name']['last']
    pais = "Pais: " + info['location']['country']
    genero = "genero: " + info['gender']
    fecha = (info['dob']['date'])
    fecha = "Fecha De Nacimiento: " + fecha[0:19].replace("T"," a las ") + " Horas"
    file.write(f"""
    <br>
    <div style="width: 1000px; margin:0 auto; border:1px solid rgb(0, 0, 0); background:linear-gradient(30deg, crimson,sienna, royalblue, indianred, purple);">
        <h1 style="text-align:center;">Bienvenido</h1>
        <center>
            <td aling = "center"; style="width: 170px;">
                <img style="width: 150px; border-radius: 35%;" src={foto} alt="Foto de {nombre}">
            </td>
        </center>
        <h3 style="text-align:center;">{titulo}</h3>
        <h3 style="text-align:center;">{nombre}</h3>
        <h3 style="text-align:center;">{apellido}</h3>
        <h3 style="text-align:center;">{pais}</h3>
        <h3 style="text-align:center;">{genero}</h3>
        <h3 style="text-align:center;">{fecha}</h3>
    </div>""")

file.write("""
</body>
</html>""")
file.close()
webbrowser.open_new_tab(nombreArchivo+".html")