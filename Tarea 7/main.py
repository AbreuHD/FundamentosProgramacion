import funciones
import dataB
import os

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
            ║                                1 = ver base de datos                        ║
            ║                                2 = Añadir Motor                             ║
            ║                                3 = Eliminar                                 ║
            ║                                4 = Exportar Mapa                            ║
            ║                                5 = Exportar Licencia                        ║
            ║                                6 = Salir                                    ║  
            ║                                                                             ║
            ╚═════════════════════════════════════════════════════════════════════════════╝ 
           """)
      
      selectOption = int(input(" : "))
      if (selectOption == 1):
          funciones.verUsuarios(main)
      elif (selectOption == 2):
          funciones.Agregar(main, dataB)
      elif (selectOption == 3):
          funciones.Eliminar(main, dataB)
      elif (selectOption == 4):
          funciones.Exportar(main, dataB)
      elif (selectOption == 5):
          funciones.ExportarLicencia(main, dataB)
      else: input("Toca enter para salir")
      
main()