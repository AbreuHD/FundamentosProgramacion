print("""
 ____    ___   ____   _          ___   _____   ___    ___
|___ \  / _ \ |___ \ / |        / _ \ |___ /  / _ \  ( _ ) 
  __) || | | |  __) || | _____ | | | |  |_ \ | | | | / _ \      
 / __/ | |_| | / __/ | ||_____|| |_| | ___) || |_| || (_) |
|_____| \___/ |_____||_|        \___/ |____/  \___/  \___/
""")

salario = int(input("Introduce tu salario: "))
tipoDeIngreso = str(input("Eres empleado o empresario? "))

if( tipoDeIngreso.lower() == "empleado"):
    print("Debes pagar el 2.87% que son", salario*0.0287, "al afp")
else:
    print("Debes pagar el 7.10% que son", salario*0.0710, "al afp")
    