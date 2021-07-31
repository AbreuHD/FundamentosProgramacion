from tkinter import *
import webbrowser

ventana = Tk()
ventana.title("Programa que genere HTML")
ventana.geometry('500x300')
ventana.resizable(0,0)

name = Entry(ventana)
name.place(x = 150, y =5, width = 200, height = 25)
name.insert(0, 'Introduce tu nombre')

bttExportar = Button(ventana, text = 'Exportar', command = lambda: exportar()).place(x = 200, y = 200, width = 100, height = 25)

apellido = Entry(ventana)
apellido.place(x = 150, y =50, width = 200, height = 25)
apellido.insert(0, 'Introduce tu apellido')

correo = Entry(ventana)
correo.place(x = 150, y =95, width = 200, height = 25)
correo.insert(0, 'Introduce tu correo')

telefono = Entry(ventana)
telefono.place(x = 150, y =140, width = 200, height = 25)
telefono.insert(0, 'Introduce tu telefono')

info = Label(ventana, text = 'Recuerda Introducir un correo valido, y si alguna caja se pone en rojo verifica lo que pusiste.').place(x = 4, y = 250)

def htmlCreation():
    
    file = open(name.get()+'.html', 'x', encoding='utf-8')
    file.write(f''' <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>2021-0308</title>
</head>
<body>
    <div style="margin-left:auto; margin-right:auto; margin-top: 250px">
        <h2 style="text-align: center;">{name.get()} {apellido.get()}</h2>
        <h3 style="text-align: center;">{correo.get()}</h3>
        <h4 style="text-align: center ">{telefono.get()}</h4>
    </div>
</body>
</html> ''')
    file.close
    webbrowser.open_new_tab(name.get()+'.html')
    
def exportar():
    name.config(bg = '#FFFFFF')
    apellido.config(bg = '#FFFFFF')
    correo.config(bg = '#FFFFFF')
    telefono.config(bg = '#FFFFFF')
    i = 0
    if(len(name.get()) == 0 or name.get() == 'Introduce tu nombre'):
        i = 1
        name.config(bg = 'red')
    if(len(apellido.get()) == 0 or apellido.get() == 'Introduce tu apellido'):
        i = 1 
        apellido.config(bg = 'red')
    if(len(correo.get()) == 0 or str(correo.get()).find('@') < 0 or str(correo.get()).find('.') < 0):
        i = 1
        correo.config(bg = 'red')
    if(len(telefono.get()) == 0 or telefono.get() == 'Introduce tu telefono'):
        i = 1
        telefono.config(bg = 'red')      
    if (i == 0):
        htmlCreation()

ventana.mainloop()