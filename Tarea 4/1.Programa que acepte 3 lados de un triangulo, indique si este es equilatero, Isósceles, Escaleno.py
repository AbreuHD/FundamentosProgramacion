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

if (n1 == n2 and n2 == n3):
    print("Es equilatero")
elif(n1 != n2 and n3 == n2 or n1 != n2 and n3 == n1 or n2 != n3 and n1 == n2 or n2 != n3 and n1 == n3):
    print("Este es un isoceles")
else: print("Es Escaleno")