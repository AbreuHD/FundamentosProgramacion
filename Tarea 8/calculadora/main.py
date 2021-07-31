from tkinter import *
ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("315x385")

countR = 1
recent = ''

vista = Entry(ventana, bg = '#1F1F1F', fg = '#FFFFFF', font = ("Helvetica", 20))
vista.place(x=0, y=50, width=315, height=75)

matricula = Label(ventana, text = '2021-0308', font = ("Times New", 20)).place(x=0, y=0, width=265, height = 50)


def datos(dat, do = 1):
    longitud = len(vista.get())
    if(vista.get() == 'Error de sintaxis'):
        vista.delete(0, END)
        
    if(do == 1):
        vista.insert(longitud, dat)
    elif(do == 2):
        vista.delete(longitud-1,longitud)
        print(longitud)
        
def resultado():
    global recent
    try:
        data = eval(vista.get())
        recent = vista.get()
        vista.delete(0, END)
        vista.insert(0,data)
    except:
        delete()
        vista.insert(0,'Error de sintaxis')

def delete():
    global recent
    recent = vista.get()
    vista.delete(0, END)
    return

    
def reciente(lastN):
    ultimo = vista.get()
    vista.delete(0, END)
    vista.insert(0, lastN)

botonRecents1 = Button(ventana, text = 'B', command = lambda: reciente(recent), bg = '#1F1F1F', fg = '#FFFFFF').place(x=265, y=0, width=50, height=50)

boton7 = Button(ventana, text = '7', command = lambda: datos('7'), bg = '#060606', fg = '#FFFFFF').place(x=0, y=177, width=80, height=52)
boton8 = Button(ventana, text = '8', command = lambda: datos('8'), bg = '#060606', fg = '#FFFFFF').place(x=80, y=177, width=80, height=52)
boton9 = Button(ventana, text = '9', command = lambda: datos('9'), bg = '#060606', fg = '#FFFFFF').place(x=160, y=177, width=80, height=52)

boton4 = Button(ventana, text = '4', command = lambda: datos('4'), bg = '#060606', fg = '#FFFFFF').place(x=0, y=229, width=80, height=52)
boton5 = Button(ventana, text = '5', command = lambda: datos('5'), bg = '#060606', fg = '#FFFFFF').place(x=80, y=229, width=80, height=52)
boton6 = Button(ventana, text = '6', command = lambda: datos('6'), bg = '#060606', fg = '#FFFFFF').place(x=160, y=229, width=80, height=52)

boton3 = Button(ventana, text = '1', command = lambda: datos('1'), bg = '#060606', fg = '#FFFFFF').place(x=0, y=281, width=80, height=52)
boton2 = Button(ventana, text = '2', command = lambda: datos('2'), bg = '#060606', fg = '#FFFFFF').place(x=80, y=281, width=80, height=52)
boton1 = Button(ventana, text = '3', command = lambda: datos('3'), bg = '#060606', fg = '#FFFFFF').place(x=160, y=281, width=80, height=52)

botonNegate = Button(ventana, text = 'DEL', command = lambda: delete(), bg = '#060606', fg = '#FFFFFF').place(x=0, y=333, width=80, height=52)
boton0 = Button(ventana, text = '0', command = lambda: datos('0'), bg = '#060606', fg = '#FFFFFF').place(x=80, y=333, width=80, height=52)
botonPoint = Button(ventana, text = '.', command = lambda: datos('.'), bg = '#060606', fg = '#FFFFFF').place(x=160, y=333, width=80, height=52)

botonMulti = Button(ventana, text = 'X', command = lambda: datos('*'), bg = '#060606', fg = '#FFFFFF').place(x=160, y=125, width=80, height=52)
botonRest = Button(ventana, text = '-', command = lambda: datos('-'), bg = '#060606', fg = '#FFFFFF').place(x=80, y=125, width=80, height=52)
botonSum = Button(ventana, text = '+', command = lambda: datos('+'), bg = '#060606', fg = '#FFFFFF').place(x=0, y=125, width=80, height=52)

botonDiv = Button(ventana, text = '/', command = lambda:datos('/'), bg = '#060606', fg = '#FFFFFF').place(x=240, y=125, width=80, height=52)
botonDel = Button(ventana, text = '◀', command = lambda: datos('x', 2), bg = '#060606', fg = '#FFFFFF').place(x=240, y=177, width=80, height=104)
botonEqual = Button(ventana, text = '=', command = lambda: resultado(), bg = '#060606', fg = '#FFFFFF').place(x=240, y=281, width=80, height=104)

ventana.resizable(0,0)
ventana.mainloop()