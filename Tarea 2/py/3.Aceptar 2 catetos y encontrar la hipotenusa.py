import math
print("""
 ____    ___   ____   _          ___   _____   ___    ___
|___ \  / _ \ |___ \ / |        / _ \ |___ /  / _ \  ( _ ) 
  __) || | | |  __) || | _____ | | | |  |_ \ | | | | / _ \      
 / __/ | |_| | / __/ | ||_____|| |_| | ___) || |_| || (_) |
|_____| \___/ |_____||_|        \___/ |____/  \___/  \___/
""")

n1 = int(input("Ingresa tu 1er Cateto: "))
n2 = int(input("Ingresa tu 2do Cateto: "))

print("La hipotenusa de dichos catetos es: ",  math.sqrt(n1**2 + n2**2))


