from tkinter import *

ventana = Tk()
ventana.title('Promedio')
ventana.geometry('400x300')
ventana.resizable(0,0)

datos = []
calc = 0

inputDatos = Entry(ventana, font = ("Times New", 10))
inputDatos.place(x=150, y=50, width = 100, height = 50)

promedio = Entry(ventana, bg = 'red')
promedio.place(x = 0, y = 0, width = 400, height = 50)

botonAgg = Button(ventana, text = 'Agregar', command = lambda: agregar())
botonAgg.place(x = 150, y = 150, width = 100, height = 50)
botonEli = Button(ventana, text = '◀', command = lambda: eliminar()).place(x = 100, y = 150, width = 50, height = 50)
botonDel = Button(ventana, text = 'Del', command = lambda: eliminar(1)).place(x = 250, y = 150, width = 50, height = 50)

signal = Label(ventana, text = 'Introduce las notas aqui ->').place(x=0, y=65)

literalP = Label(ventana,fg = 'green', font = ("Times New", 20))
literalP.place(x=325, y=75)

datoShow = Entry(ventana,  font = ("Times New", 10))
datoShow.place(x=0, y=250, width = 400, height = 50)


def agregar():
    if(len(datos) == 3):
        botonAgg.configure(text = 'Promediar')
    if(len(datos) != 4):
        try:
            datos.append(float(inputDatos.get()))
            promedio.delete(0,END)
        except:
            promedio.delete(0,END)
            promedio.insert(0,'Debes introducir datos validos')
    else:
#        if(len(promedio.get()) ==0):
        promediar()
    show()
    
def promediar():
    global calc
    calc = 0
    for a in datos:
        calc += int(a)
    finalP = calc/len(datos)
    promedio.delete(0, END)
    promedio.insert(0, finalP)
    if(finalP >= 90):
        literalP.config(text = 'A')
    elif (finalP >= 80):
        literalP.config(text = 'B')
    elif (finalP >= 70):
        literalP.config(text = 'C')    
    else:
        literalP.config(text = 'F')
        literalP.config(fg = 'red')
    
def eliminar(select = 0):
    if(select == 0):
        print(len(datos)-1)
        datos.pop(len(datos)-1)
        botonAgg.configure(text = 'Agregar')
        literalP.config(text = '')
        literalP.config(fg = 'green')
    else:
        datos.clear()
        botonAgg.configure(text = 'Agregar')
        literalP.config(text = '')
        literalP.config(fg = 'green')
    show()

def show():
    datoShow.delete(0, END)
    data = 0
    texto = ''
    for show in datos:
        data +=1
        texto += f'Nota{data}: {show} '
        datoShow.delete(0, END)
        datoShow.insert(0,texto)
    return
ventana.mainloop()
