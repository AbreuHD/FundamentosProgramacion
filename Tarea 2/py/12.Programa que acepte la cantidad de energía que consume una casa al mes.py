print("""
 ____    ___   ____   _          ___   _____   ___    ___
|___ \  / _ \ |___ \ / |        / _ \ |___ /  / _ \  ( _ ) 
  __) || | | |  __) || | _____ | | | |  |_ \ | | | | / _ \      
 / __/ | |_| | / __/ | ||_____|| |_| | ___) || |_| || (_) |
|_____| \___/ |_____||_|        \___/ |____/  \___/  \___/
""")

kWh = int(input("Cuantos  kWh consumes mensual? "))

if (kWh > 700):
    print("Debes pagar ", kWh*11.10)
elif (kWh > 301):
    print("Debes pagar ", kWh*10.86)
elif (kWh > 201):
    print("Debes pagar ", kWh*6.97)
else:
    print("Debes pagar ", kWh*4.44)
    