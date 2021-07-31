import datetime
print("""
 ____    ___   ____   _          ___   _____   ___    ___
|___ \  / _ \ |___ \ / |        / _ \ |___ /  / _ \  ( _ ) 
  __) || | | |  __) || | _____ | | | |  |_ \ | | | | / _ \      
 / __/ | |_| | / __/ | ||_____|| |_| | ___) || |_| || (_) |
|_____| \___/ |_____||_|        \___/ |____/  \___/  \___/
""")

hoy = datetime.date.today()
dia = int(input("Ingresa el dia que naciste: "))
mes = int(input("Ingresa tu mes de nacimiento en formato numero: "))
age = int(input("Ingresa tu año de nacimiento: "))

age = hoy.year - age

if (mes < int(hoy.strftime("%m"))):
    print("Tienes ", age, " años")
    
elif(dia <= int(hoy.strftime("%d")) and mes == int(hoy.strftime("%m"))):
    print("Tienes ", age, " años")    

else:
    print("Tienes ", age-1, " años")    
