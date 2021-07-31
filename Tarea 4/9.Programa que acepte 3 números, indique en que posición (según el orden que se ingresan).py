import numpy as np 
print("""
 ____    ___   ____   _          ___   _____   ___    ___
|___ \  / _ \ |___ \ / |        / _ \ |___ /  / _ \  ( _ ) 
  __) || | | |  __) || | _____ | | | |  |_ \ | | | | / _ \      
 / __/ | |_| | / __/ | ||_____|| |_| | ___) || |_| || (_) |
|_____| \___/ |_____||_|        \___/ |____/  \___/  \___/
""")
contador = 0
i = 0
numeros = np.array([int(input("Introduce tu 1er numero: ")),
                    int(input("Introduce tu 2do numero: ")),
                    int(input("Introduce tu 3er numero: "))])
comparador = [0,0,0]

while(contador < 3):
  i = 0
  while (i<3):
        if(comparador[contador] < numeros[i] and comparador[0] != numeros[i] and comparador[1] != numeros[i] and comparador[2] != numeros[i]): 
          comparador[contador] = numeros[i]
        i+=1
  contador +=1

contador = 0
while(contador < 3):
      i = 0
      while (i < 3):
            doble = 0
            if (comparador[contador] == numeros[i]): 
              print("Tu numero ", comparador[contador], "es el numero", i+1, "que introdujiste.")
            i += 1
      contador += 1
if(numeros[0] == numeros[2]):
  print("El 1ro y el ultimo en orden de entrada son iguales")
