print("""
 ____    ___   ____   _          ___   _____   ___    ___
|___ \  / _ \ |___ \ / |        / _ \ |___ /  / _ \  ( _ ) 
  __) || | | |  __) || | _____ | | | |  |_ \ | | | | / _ \      
 / __/ | |_| | / __/ | ||_____|| |_| | ___) || |_| || (_) |
|_____| \___/ |_____||_|        \___/ |____/  \___/  \___/
""")
pan = int(input("Cuantos panes tienes? ")) #1
carne = int(input("Cuantas carnes tienes? ")) #2
tocineta = str(input("Cuantas libras de tocineta tienes? se permite el formato normal en libras o con / ")) #1/5
cantidadTotal = pan
if(tocineta.count('/') == 1):
    counter = tocineta.index('/')
    tocineta1 = int(tocineta[:counter].replace(' ', ''))
    tocineta2 = int(tocineta[counter+1:].replace(' ', ''))
    tocineta = tocineta1/tocineta2
else:
    tocineta = int(tocineta)

tocineta = int(tocineta/0.2)

if(cantidadTotal > carne):
    cantidadTotal = carne
elif(cantidadTotal > tocineta):
    cantidadTotal = tocineta
    
print("Con esos ingredientes puedes hacer ", cantidadTotal, " Tocinetas")