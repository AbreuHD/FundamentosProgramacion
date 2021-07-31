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

if (n1 < 90 and n2 < 90 and n3 < 90):
    print("Es Acutangulo")
elif (n1 > 90 or n2 > 90 or n3 > 90):
    print("Es Obstusngulo")
elif (n1 == 90 or n2 == 90 or n3 == 90):
    print("Es Rectangulo")