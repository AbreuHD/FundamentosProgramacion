import webbrowser
print("""
 ____    ___   ____   _          ___   _____   ___    ___
|___ \  / _ \ |___ \ / |        / _ \ |___ /  / _ \  ( _ ) 
  __) || | | |  __) || | _____ | | | |  |_ \ | | | | / _ \      
 / __/ | |_| | / __/ | ||_____|| |_| | ___) || |_| || (_) |
|_____| \___/ |_____||_|        \___/ |____/  \___/  \___/
""")

nombre = str(input("Introduce tu nombre: "))
apellido = str(input("Introduce tu apellido: "))
telefono = str(input("Introduce tu telefono: "))
email = str(input("Introduce tu correo: "))
nameFile = str(input("Introduce el nombre con el que quieres guardar tu archivo: "))

html = f"""<!-- programa que acepte un nombre, apellido, telefono y email. 
Guarde estos datos en un archivo html bonito, con colores en su computadora y luego muéstrelo en el navegador.
-->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>name {nombre}</title>
</head>
<body>
    <div style="width: 1000px; margin:0 auto; border:1px solid rgb(0, 0, 0); background:linear-gradient(30deg, crimson,sienna, royalblue, indianred, purple);
    ">
        <h1 style="text-align:center;">Bienvenido</h1>
        <h3 style="text-align:center;">{nombre}</h3>
        <h3 style="text-align:center;">{apellido}</h3>
        <h3 style="text-align:center;">{telefono}</h3>
        <h3 style="text-align:center;"><a href="mailto:{email}">{email}</a></h3>

    </div>
</body>
</html>"""

file = open(nameFile+".html", "x")
file.write(html)
file.close()
webbrowser.open_new_tab(nameFile+".html")