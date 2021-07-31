import requests
import json

print("""
 ____    ___   ____   _          ___   _____   ___    ___
|___ \  / _ \ |___ \ / |        / _ \ |___ /  / _ \  ( _ ) 
  __) || | | |  __) || | _____ | | | |  |_ \ | | | | / _ \      
 / __/ | |_| | / __/ | ||_____|| |_| | ___) || |_| || (_) |
|_____| \___/ |_____||_|        \___/ |____/  \___/  \___/
""")

busqueda = str(input("Ingresa lo que quieres buscar: "))
urlApi = requests.get(f'https://es.wikipedia.org/w/api.php?action=query&list=search&srprop=snippet&format=json&origin=*&utf8=&srsearch={busqueda}').json()

print("*********************************************")

for info in urlApi['query']['search']:
    print("Titulo", info['title'])
    descripcion = info['snippet']
    print("Descripcion:", descripcion.replace('span class=\"searchmatch\">','').replace('<','').replace('/span>',''))
    print("*********************************************")

