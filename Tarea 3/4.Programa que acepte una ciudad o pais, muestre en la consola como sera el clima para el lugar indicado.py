import requests
import json

print("""
 ____    ___   ____   _          ___   _____   ___    ___
|___ \  / _ \ |___ \ / |        / _ \ |___ /  / _ \  ( _ ) 
  __) || | | |  __) || | _____ | | | |  |_ \ | | | | / _ \      
 / __/ | |_| | / __/ | ||_____|| |_| | ___) || |_| || (_) |
|_____| \___/ |_____||_|        \___/ |____/  \___/  \___/
""")

city = str(input("Ingresa el nombre de tu ciudad: "))
apiWeather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=b832de3a99be845ec1921540251d7b09").json()

temperatura = float(apiWeather['main']['temp'])
temperaturaMax = float(apiWeather['main']['temp_max'])
temperaturaMin = float(apiWeather['main']['temp_min'])
sensacionTermica = float(apiWeather['main']['feels_like'])

print("*********************************************")
print("Pais:", apiWeather['sys']['country'])
print("Habra:", apiWeather['weather'][0]['main'])
print("La temperatura es", int(temperatura-273.15),"°C")
print("La temperatura maxima es", int(temperaturaMax-273.15),"°C")
print("La temperatura minima es", int(temperaturaMin-273.15),"°C")
print("La sensacion termica es", int(sensacionTermica-273.15),"°C")
print("Humedad:", apiWeather['main']['humidity'],"%")
print("*********************************************")