print("""
 ____    ___   ____   _          ___   _____   ___    ___
|___ \  / _ \ |___ \ / |        / _ \ |___ /  / _ \  ( _ ) 
  __) || | | |  __) || | _____ | | | |  |_ \ | | | | / _ \      
 / __/ | |_| | / __/ | ||_____|| |_| | ___) || |_| || (_) |
|_____| \___/ |_____||_|        \___/ |____/  \___/  \___/
""")

kmPorGalon = int(input("Introduce la cantidad de km por galon que da tu automovil: "))
distancia = int(input("Introduce la distancia en Km que piensas recorrer: "))
kmPorGalon = kmPorGalon*distancia
print("La gasolina regular esta a 239.30 entonces debes comprar ", kmPorGalon*239.30, " pesos en gasolina para hacer dicho viaje")