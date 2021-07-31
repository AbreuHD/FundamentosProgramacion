import requests
import json
import webbrowser
import datetime

# 2021-0308
# Jefferson Abreu Martinez
# 27-6-2021

hoy = datetime.date.today()
cedula = str(input("Introduce tu cedula: "))
cedula = cedula.replace("-","")
nameFile = str(input("Introduce el nombre que le daras al archivo html"))

datos = requests.get(f"https://api.adamix.net/apec/cedula/{cedula}").json()
nombreCompleto = datos['Nombres'] + " " + datos['Apellido1'] + " " + datos['Apellido2']
fecha = datos['FechaNacimiento'][0:10]
fechaDeNacimiento = fecha.split('-')
age = hoy.year - int(fechaDeNacimiento[0])
image = datos['foto']
genero = datos['IdSexo']
if(genero == "M"):
    genero = "Masculino"
else: genero = "Femenino"

signosZ = [['Acuario', 1, 20], 
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

for i in range(len(signosZ)):
    if(int(fechaDeNacimiento[1]) == signosZ[i][1]):
        if(int(fechaDeNacimiento[2]) < signosZ[i][2]):
            signo = signosZ[i-1][0]
        else: signo = signosZ[i][0]
        
if(int(fechaDeNacimiento[1]) < int(hoy.strftime("%m"))):
    age = age
elif(int(fechaDeNacimiento[2]) <= int(hoy.strftime("%d")) and int(fechaDeNacimiento[1]) == int(hoy.strftime("%m"))):
    age = age
else: age = age-1

html= f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cedula</title>
</head>
<body style="background:url(https://wallpapercave.com/wp/wp7224728.jpg);">
    <div style="margin-left:auto; margin-right:auto; border-radius: 25px; border:2px solid #ffffff; width: 700px; height:350px; background:linear-gradient(-30deg, rgb(146,216,33), rgb(255,255,255))">
        <h2 style="text-align: center;">Republica Dominicana</h2>
        <h3 style="text-align: center;">Junta Central Dominicana</h3>
        <img style="float:left; border-radius:25px; margin-left:15px; margin-right:5px" src="https://api.adamix.net/apec/foto2/00100782788" width="184"; height="219">
        <h4 style="margin-right: 200px; text-align:center">{nombreCompleto}</h4>
        <h4 style="margin-right: 200px; text-align:center">{fecha}</h4>
        <h4 style="margin-right: 200px; text-align:center">{age}</h4>
        <h4 style="margin-right: 200px; text-align:center">{signo}</h4>
        <h4 style="margin-right: 200px; text-align:center">{genero}</h4>
    </div>
    
</body>
</html>"""

file = open(nameFile+".html", "x")
file.write(html)
file.close
webbrowser.open_new_tab(nameFile+'.html')