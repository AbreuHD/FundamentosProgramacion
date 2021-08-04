import datab
import funciones

def main():
    print("""
            ╔═════════════════════════════════════════════════════════════════════════════╗
            ║                                                                             ║
            ║                    ███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗                    ║
            ║                    ████╗░████║██╔════╝████╗░██║██║░░░██║                    ║
            ║                    ██╔████╔██║█████╗░░██╔██╗██║██║░░░██║                    ║
            ║                    ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║                    ║
            ║                    ██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝                    ║
            ║                    ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░                    ║
            ║≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈║
            ║               Introduce un numero para hacer dicha accion.                  ║
            ║                                                                             ║
            ║                                1 = ver querellas                            ║
            ║                                2 = agregar querella                         ║
            ║                                3 = editar querella                          ║
            ║                                4 = Exportar                                 ║
            ║                                5 = Salir                                    ║  
            ║                                                                             ║
            ╚═════════════════════════════════════════════════════════════════════════════╝  
    """)
    seleccion = funciones.vericarDatos(": ", 1)
    if(seleccion == 1):
        funciones.ver(main, 1)
    elif(seleccion == 2):
        funciones.agregar(main)
    elif(seleccion == 3):
        funciones.editar(main)
    elif(seleccion == 4):
        funciones.exportar(main)
    elif (seleccion == 5):
        input("Presiona enter para salir")
    else:
        input("Debe introducir uno de los datos que estan en el menu, presiona enter para continuar")
        main()

main()