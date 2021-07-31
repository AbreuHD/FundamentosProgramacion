import requests
import json

print("""
 ____    ___   ____   _          ___   _____   ___    ___
|___ \  / _ \ |___ \ / |        / _ \ |___ /  / _ \  ( _ ) 
  __) || | | |  __) || | _____ | | | |  |_ \ | | | | / _ \      
 / __/ | |_| | / __/ | ||_____|| |_| | ___) || |_| || (_) |
|_____| \___/ |_____||_|        \___/ |____/  \___/  \___/
""")

numeroDeUsuarios = int(input("Ingresa el numero de usuarios que desea generar: "))
datos = requests.get(f"https://randomuser.me/api/?results={numeroDeUsuarios}").json()

print("*********************************************")

for info in datos['results']:
    print("Titulo:", info['name']['title'])
    print("Nombre:", info['name']['first'])
    print("Apellido:", info['name']['last'])
    print("Pais:", info['location']['country'])
    fecha = (info['dob']['date'])
    print("Fecha De Nacimiento:", fecha[0:19].replace("T"," a las "), "Horas")
    print("Edad:", info['dob']['age'])
    print("*********************************************")