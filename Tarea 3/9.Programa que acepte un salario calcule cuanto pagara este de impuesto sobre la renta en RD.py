print("""
 ____    ___   ____   _          ___   _____   ___    ___
|___ \  / _ \ |___ \ / |        / _ \ |___ /  / _ \  ( _ ) 
  __) || | | |  __) || | _____ | | | |  |_ \ | | | | / _ \      
 / __/ | |_| | / __/ | ||_____|| |_| | ___) || |_| || (_) |
|_____| \___/ |_____||_|        \___/ |____/  \___/  \___/
""")

sueldoBruto = int(input("Introduce cuanto ganas mensualmente: "))
sueldoBruto = sueldoBruto*12

if (sueldoBruto > 867123.1):
    sueldoNeto = sueldoBruto-867123.1
    sueldoNeto = sueldoNeto*0.25
    sueldoNeto = sueldoNeto+79776
    sueldoNeto = sueldoBruto-sueldoNeto
    print("Te quedan", sueldoNeto/12, "de los", sueldoBruto/12, "Iniciales al aplicar el pago de impuestos")
    
elif (sueldoBruto > 624329.01):
    sueldoNeto = sueldoBruto-624329.01
    sueldoNeto = sueldoNeto*0.2
    sueldoNeto = sueldoNeto+31216
    sueldoNeto = sueldoBruto-sueldoNeto
    print("Te quedan", sueldoNeto/12, "de los", sueldoBruto/12, "Iniciales al aplicar el pago de impuestos")
    
elif (sueldoBruto > 416220.01):
    sueldoNeto = sueldoBruto-416220.01
    sueldoNeto = sueldoNeto*0.15
    sueldoNeto = sueldoBruto-sueldoNeto
    print("Te quedan", sueldoNeto/12, "de los", sueldoBruto/12, "Iniciales al aplicar el pago de impuestos")
    
else:
    print("Tu sueldo sigue siendo de", sueldoBruto/12, "tu estas excento de impuestos")
    
    

