#stark03

from data_stark import lista_personajes

from funciones import *

import sys

opcion = None

aux_lista_personajes = [] # aca vamos a guardar las copias de los dicc. de la lista_personajes original

aux_lista_normalizada = False

bandera_primera_vez_opcion_a = True

while not opcion == "X":
    
#     for heroe in lista_personajes:
          
#         print(heroe)

#     print("---------------------")    


    print("A. Normalizar datos (No se debe poder acceder a los otros puntos)\n"
            "B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB\n"
            "C. Recorrer la lista y determinar cuál es el superhéroe más alto de género F\n"
            "D. Recorrer la lista y determinar cuál es el superhéroe más alto de género M\n"
            "E. Recorrer la lista y determinar cuál es el superhéroe más débil de género M\n"
            "F. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB\n"
            "G. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB\n"
            "H. Determinar cuántos superhéroes tienen cada tipo de color de ojos.\n"
            "I. Determinar cuántos superhéroes tienen cada tipo de color de pelo.\n"
            "J. Listar todos los superhéroes agrupados por color de ojos.\n"
            "K. Listar todos los superhéroes agrupados por tipo de inteligencia \n")
    
    print(f"El len de la lista_personajes {len(lista_personajes)}")
    
    opcion = input("Por favor elija una opcion: ")

    opcion = opcion.lower()

    match opcion:
         
        case "a":

                if bandera_primera_vez_opcion_a:
                       
                       bandera_primera_vez_opcion_a = False

                       aux_lista_normalizada = stark_normalizar_datos(lista_personajes, "\nDatos Normalizados\n", "\nHubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente\n")

                else:
                       
                       print("\ndatos ya normalizados previamente\n")
                       

        case "b":
                  
                  if aux_lista_normalizada == True:
                         
                         pass
                  
                  else:
                         
                         print("\nTenga a bien normalizar los datos previamente\n")
         
           
        case "x":

                opcion = input("Desea cerrar el programa? (s/n): ")

                while not opcion == 's' and not opcion == 'n':

                        opcion = print("Elija una opcion correcta (s/n): ")

                if opcion == "s":

                        print("Adios!!!\n")

                        break
                