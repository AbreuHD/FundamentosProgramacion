from peewee import SqliteDatabase, AutoField, CharField, DateField, ForeignKeyField, Model, IntegerField
import time
import os
import funciones
from playsound import playsound

print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║  ██████╗░██╗███████╗███╗░░██╗██╗░░░██╗███████╗███╗░░██╗██╗██████╗░░█████╗░  ║ 
║  ██╔══██╗██║██╔════╝████╗░██║██║░░░██║██╔════╝████╗░██║██║██╔══██╗██╔══██╗  ║
║  ██████╦╝██║█████╗░░██╔██╗██║╚██╗░██╔╝█████╗░░██╔██╗██║██║██║░░██║██║░░██║  ║
║  ██╔══██╗██║██╔══╝░░██║╚████║░╚████╔╝░██╔══╝░░██║╚████║██║██║░░██║██║░░██║  ║
║  ██████╦╝██║███████╗██║░╚███║░░╚██╔╝░░███████╗██║░╚███║██║██████╔╝╚█████╔╝  ║
║  ╚═════╝░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═╝╚═════╝░░╚════╝░  ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝ 
""")
playsound('sound/Bienvenido.mp3')
time.sleep(1)
os.system('cls')

def main():
      os.system('cls')
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
            ║                                1 = ver datos                                ║
            ║                                2 = Agregar                                  ║
            ║                                3 = Modificar                                ║
            ║                                4 = Eliminar                                 ║
            ║                                5 = Exportar                                 ║ 
            ║                                6 = Salir                                    ║  
            ║                                                                             ║
            ╚═════════════════════════════════════════════════════════════════════════════╝ 
           """)

      playsound('sound/seleccion.mp3')
      seleccion = int(input())
      if (seleccion == 1):
            funciones.mostrar(main)
      elif (seleccion == 2):
            funciones.agregar(main)
      elif (seleccion == 3):
            funciones.modificar(main)
      elif (seleccion == 4):
            funciones.eliminar(main)
      elif (seleccion == 5):
            funciones.exportar()
      elif (seleccion == 6):
            input('Presiona Enter para salir ')
      else: print('introduce un numero valido')
      
main()