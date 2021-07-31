print("""
 ____    ___   ____   _          ___   _____   ___    ___
|___ \  / _ \ |___ \ / |        / _ \ |___ /  / _ \  ( _ ) 
  __) || | | |  __) || | _____ | | | |  |_ \ | | | | / _ \      
 / __/ | |_| | / __/ | ||_____|| |_| | ___) || |_| || (_) |
|_____| \___/ |_____||_|        \___/ |____/  \___/  \___/
""")
n1 = float(input("Introduce el tamaño del primer lado: "))
n2 = float(input("Introduce el tamaño del primer lado: "))
n3 = float(input("Introduce el tamaño del primer lado: "))
n4 = float(input("Introduce el tamaño del primer lado: "))
if(n1 == n2 and n2 == n3 and n3 == n4):
    print("Tu figura es un cuadrado")
else: print("Tu figura no es un cuadrado")