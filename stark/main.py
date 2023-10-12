from data_stark import lista_personajes

from funciones import *

opcion = None

while not opcion == "X":

    print("A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB\n" #ok
            "B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F\n" #ok
            "C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M\n" #ok
            "D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M\n" #ok
            "E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB\n" #ok
            "F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB\n" #ok
            "G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.\n" #ok
            "H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.\n"
            "I. Listar todos los superhéroes agrupados por color de ojos.\n" #ok
            "J. Listar todos los superhéroes agrupados por tipo de inteligencia\n") #ok
    
    print(f"El len de la lista_personajes {len(lista_personajes)}")
    
    opcion = input("Por favor elija una opcion: ")

    opcion = opcion.lower()

    match opcion:
         
        case "a":
              
                if contar_cantidad_de_heroes_por_genero(lista_personajes, "nb") == 0:
                    
                    print("\nNo existen superheroes de ese género\n")
                    
                else:
                    
                    imprimir_nombre_heroes_genero(lista_personajes, "nb") # esto es de ejemplo, lo que pide es lo de arriba

        case "b":

                # conseguimos la maxima altura

                aux_mayor_altura_femeninos = obtener_max_min_altura_por_opcion_y_genero(lista_personajes,"max","f")

                # usamos ese valor conseguido para filtrar el print

                print("\nEl superheroe femenino mas alto es:\n")
                imprimir_nombre_heroes_por_genero_y_valor(lista_personajes, "f", aux_mayor_altura_femeninos)

        case "c":
              
                aux_mayor_altura_masculino = obtener_max_min_altura_por_opcion_y_genero(lista_personajes,"max","m")

                # usamos ese valor conseguido para filtrar el print

                print("\nEl superheroe masculino mas alto es:\n")
                imprimir_nombre_heroes_por_genero_y_valor(lista_personajes, "m", aux_mayor_altura_masculino)

        case "d":
              
                aux_menor_fuerza_masculino = obtener_max_min_fuerza_por_opcion_y_genero(lista_personajes,"min","m")

                # usamos ese valor conseguido para filtrar el print

                print("\nEl superheroe masculino mas debil es:\n")
                imprimir_nombre_heroes_por_genero_y_valor_int(lista_personajes, "m", aux_menor_fuerza_masculino)

        case "e":
              
                if contar_cantidad_de_heroes_por_genero(lista_personajes, "nb") == 0:
                    
                    print("\nNo existen superheroes de ese género\n")

                else:
                    
                    aux_menor_fuerza_nb = obtener_max_min_fuerza_por_opcion_y_genero(lista_personajes, "min", "nb")

                    # usamos ese valor conseguido para filtrar el print

                    print("\nEl superheroe masculino mas debil es:\n")
                    imprimir_nombre_heroes_por_genero_y_valor_int(lista_personajes, "nb", aux_menor_fuerza_nb)

        case "f":

                if contar_cantidad_de_heroes_por_genero(lista_personajes, "nb") == 0:
                
                    print("\nNo existen superheroes de ese género\n")
                
                else:
                    
                    aux_cantidad_heroes = contar_cantidad_de_heroes_por_genero(lista_personajes, "nb")

                    aux_suma_fuerzas = sumar_fuerzas_de_heroes_por_genero(lista_personajes, "nb")

                    print(obtener_promedio_fuerzas(aux_suma_fuerzas, aux_cantidad_heroes))

        case "g":

                aux_lista_color_ojos = obtener_valor_de_campo_especifico(lista_personajes, "color_ojos")

                imprimir_cantidad_color_ojos(aux_lista_color_ojos, lista_personajes)
          
        case "h":

                aux_lista_color_pelo = obtener_valor_de_campo_color_pelo(lista_personajes, "color_pelo")

                imprimir_cantidad_color_pelo(aux_lista_color_pelo, lista_personajes)

        case "i":
                
                aux_lista_color_ojos = obtener_valor_de_campo_especifico(lista_personajes, "color_ojos")

                imprimir_heroes_por_colores_de_ojo(aux_lista_color_ojos, lista_personajes)

        case "j":
                

                aux_lista_inteligencia = obtener_valor_de_campo_especifico(lista_personajes, "inteligencia")

                imprimir_heroes_por_inteligencias(aux_lista_inteligencia, lista_personajes)
                
            
            
        case "x":

                opcion = input("Desea cerrar el programa? (s/n): ")

                while not opcion == 's' and not opcion == 'n':

                    opcion = print("Elija una opcion correcta (s/n): ")

                if opcion == "s":

                    print("Adios!!!\n")

                    break
              
             
    

     
    

                
              
              


        # opciones tp 1
        # case "a":

        #     imprimir_valores(lista_personajes)
            
        # case "b":

        #     #obtener_fuerzas_de_heroes(lista_personajes, lista_fuerzas)
                    
        #     aux_mayor_fuerza = obtener_mayor_fuerza(lista_personajes)

        #     #cargar_heroes_mayor_fuerza(lista_personajes, lista_heroes_mayor_fuerza, aux_mayor_fuerza)

        #     imprimir_identidad_y_peso(lista_personajes, aux_mayor_fuerza)

        # case "c":

        #     #obtener_alturas_de_heroes(lista_personajes, lista_alturas)

        #     aux_menor_altura = obtener_menor_altura(lista_personajes)

        #     #cargar_heroes_menor_altura(lista_personajes, lista_heroes_menor_altura, aux_menor_altura)

        #     imprimir_nombre_e_identidad(lista_personajes, aux_menor_altura)

        # case "d":

        #     #obtener_peso_de_heroes_masculinos(lista_personajes, lista_pesos_masculinos)

        #     aux_suma_pesos = sumar_pesos_de_heroes_masculinos(lista_personajes)

        #     aux_cantidad_masculinos = contar_cantidad_de_heroes_masculinos(lista_personajes)

        #     aux_promedio_pesos_masculinos = obtener_promedio_pesos_masculinos(aux_suma_pesos, aux_cantidad_masculinos)

        #     print(f"El promedio de los pesos masculinos es: {aux_promedio_pesos_masculinos:.2f}")

        # case "e":

        #     #obtener_fuerza_de_heroes_femeninos(lista_personajes, lista_fuerzas_femeninos)

        #     aux_suma_fuerzas = sumar_fuerzas_de_heroes_femeninos(lista_personajes)

        #     aux_cantidad_femeninos = contar_cantidad_de_heroes_femeninos(lista_personajes)

        #     aux_promedio_fuerzas_femeninas = obtener_promedio_fuerzas_femeninas(aux_suma_fuerzas, aux_cantidad_femeninos)

        #     imprimir_nombre_y_peso_superior_promedio_femenino(lista_personajes, aux_promedio_fuerzas_femeninas)
            
        # case "f":

        #     print("Adios!\n")
        #     break

       

