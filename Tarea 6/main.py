import os
import funciones
import db
import config 

print("""
 ____    ___   ____   _          ___   _____   ___    ___
|___ \  / _ \ |___ \ / |        / _ \ |___ /  / _ \  ( _ ) 
  __) || | | |  __) || | _____ | | | |  |_ \ | | | | / _ \      
 / __/ | |_| | / __/ | ||_____|| |_| | ___) || |_| || (_) |
|_____| \___/ |_____||_|        \___/ |____/  \___/  \___/
""")

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
            ║                                1 = ver usuarios registrados                 ║
            ║                                2 = Vacunacion                               ║
            ║                                3 = Exportar                                 ║
            ║                                4 = Configuracion                            ║
            ║                                5 = Salir                                    ║  
            ║                                                                             ║
            ╚═════════════════════════════════════════════════════════════════════════════╝ 
           """)
      
      selectOption = int(input(" : "))
      if (selectOption == 1):
          funciones.ver(main)
      elif (selectOption == 2):
          funciones.vacunacion(main, db.Paciente)
      elif (selectOption == 3):
          funciones.Exportar(main)
      elif (selectOption == 4):
          config.configuracion(main, funciones)
      else: input("Toca enter para salir")
      
main()