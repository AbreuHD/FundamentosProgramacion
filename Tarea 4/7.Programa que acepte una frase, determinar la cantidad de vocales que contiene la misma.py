print("""
 ____    ___   ____   _          ___   _____   ___    ___
|___ \  / _ \ |___ \ / |        / _ \ |___ /  / _ \  ( _ ) 
  __) || | | |  __) || | _____ | | | |  |_ \ | | | | / _ \      
 / __/ | |_| | / __/ | ||_____|| |_| | ___) || |_| || (_) |
|_____| \___/ |_____||_|        \___/ |____/  \___/  \___/
""")
palabra = str(input("Introduce tu palabra o frase: "))

cantidad = 0
for puente in palabra.lower():
    if (puente == 'a' or puente == 'e' or puente == 'i' or puente == 'o' or puente == 'u'):
        cantidad += 1
print("Tu frase o palabra tiene", cantidad, "vocales")