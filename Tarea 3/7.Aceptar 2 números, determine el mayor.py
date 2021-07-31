print("""
 ____    ___   ____   _          ___   _____   ___    ___
|___ \  / _ \ |___ \ / |        / _ \ |___ /  / _ \  ( _ ) 
  __) || | | |  __) || | _____ | | | |  |_ \ | | | | / _ \      
 / __/ | |_| | / __/ | ||_____|| |_| | ___) || |_| || (_) |
|_____| \___/ |_____||_|        \___/ |____/  \___/  \___/
""")

n1 = int(input("Introduce el primer numero: "))
n2 = int(input("Introduce el segundo numero: "))
if (n1 < n2):
    print(n2, " es el numero mas grande")
else:
    print(n1, " es el numero mas grande")
