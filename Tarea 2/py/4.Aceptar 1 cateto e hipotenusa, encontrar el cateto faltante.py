import math
print("""
 ____    ___   ____   _          ___   _____   ___    ___
|___ \  / _ \ |___ \ / |        / _ \ |___ /  / _ \  ( _ ) 
  __) || | | |  __) || | _____ | | | |  |_ \ | | | | / _ \      
 / __/ | |_| | / __/ | ||_____|| |_| | ___) || |_| || (_) |
|_____| \___/ |_____||_|        \___/ |____/  \___/  \___/
""")

cateto1 = int(input("Introduce el cateto 1: "))
hipotenusa = int(input("Introduce la hipotenusa: "))

print("EL cateto faltante es: ",  math.sqrt(hipotenusa**2 - cateto1**2))