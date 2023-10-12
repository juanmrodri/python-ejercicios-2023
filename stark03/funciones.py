import re

# esta funcion ya no va mas, la dejo para sacar como esta armado el recuadro
# def imprimir_valores(lista_personajes:list):

#     print(f"{'Nombre' :^20} | {'identidad' :^30} | {'empresa' :^15} | {'altura' :^20} | {'peso' :^20} | {'genero' :^7} | {'color_ojos' :^25} | {'color_pelo' :^15} | {'fuerza' :^7} | {'inteligencia' :^10}")
            
#     print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    
#     for heroe in lista_personajes:

#         print(f"{heroe['nombre'] : ^20} | {heroe['identidad']:^30} | {heroe['empresa']:^15} | {heroe['altura']:^20} | {heroe['peso']:^20} | {heroe['genero']:^7} | {heroe['color_ojos']:^25} | {heroe['color_pelo']:^15} | {heroe['fuerza']:^7} | {heroe['inteligencia']:^10}")
    
#     print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# para tp2

def imprimir_nombre_heroes_genero(lista_personajes, genero):

    aux_genero = genero.upper()

    print(f" | {'nombre' :^30} | ")

    print("---------------------------------------------------------")
   
    for heroe in lista_personajes:
        
        if heroe['genero'] == aux_genero:
                
            print(f" | {heroe['nombre']:^30} | ")

    print("---------------------------------------------------------")

def imprimir_nombre_heroes_por_genero_y_valor(lista_personajes, genero, valor):

    aux_genero = genero.upper()

    print(f" | {'nombre' :^30} | ")

    print("---------------------------------------------------------")
   
    for heroe in lista_personajes:
        
        if heroe['genero'] == aux_genero and float(heroe['altura']) == valor:
                
            print(f" | {heroe['nombre']:^30} | ")

    print("---------------------------------------------------------")

def imprimir_nombre_heroes_por_genero_y_valor_int(lista_personajes, genero, valor):

    aux_genero = genero.upper()

    print(f" | {'nombre' :^30} | ")

    print("---------------------------------------------------------")
   
    for heroe in lista_personajes:
        
        if heroe['genero'] == aux_genero and int(heroe['fuerza']) == valor:
                
            print(f" | {heroe['nombre']:^30} | ")

    print("---------------------------------------------------------")


def contar_cantidad_de_heroes_por_genero(lista_personajes:list, opcion:str)->int:
     
    aux_contador = 0

    aux_opcion = opcion.upper()

    for heroe in lista_personajes:
        
        if heroe['genero'] == aux_opcion:
            
            aux_contador = aux_contador+1

    return aux_contador

def obtener_max_min_altura_por_opcion_y_genero(lista_personajes:list, opcion:str, genero:str)->float:

    bandera_primera_vuelta = True

    aux_genero = genero.upper()

    aux_return = None # esto lo sacamos dependiendo de la opcion - max o min

    for heroe in lista_personajes:

            #aca filtramos por genero
            if heroe['genero'] == aux_genero:

                if bandera_primera_vuelta == True:

                    bandera_primera_vuelta = False
                    altura_minima = float(heroe['altura'])
                    altura_maxima = float(heroe['altura'])

                elif float(heroe['altura']) > altura_maxima:

                    altura_maxima = float(heroe['altura'])

                elif float(heroe['altura']) < altura_minima:

                    altura_minima = float(heroe['altura'])

    if opcion == "max":

        aux_return = altura_maxima

    elif opcion == "min":

        aux_return = altura_minima
   
    return aux_return

def obtener_max_min_fuerza_por_opcion_y_genero(lista_personajes:list, opcion:str, genero:str)->float:

    bandera_primera_vuelta = True

    aux_genero = genero.upper()

    aux_return = None # esto lo sacamos dependiendo de la opcion - max o min

    for heroe in lista_personajes:

            #aca filtramos por genero
            if heroe['genero'] == aux_genero:

                if bandera_primera_vuelta == True:

                    bandera_primera_vuelta = False
                    fuerza_minima = int(heroe['fuerza'])
                    fuerza_maxima = int(heroe['fuerza'])

                elif int(heroe['fuerza']) > fuerza_maxima:

                    fuerza_maxima = float(heroe['fuerza'])

                elif int(heroe['fuerza']) < fuerza_minima:

                    fuerza_minima = int(heroe['fuerza'])

    if opcion == "max":

        aux_return = fuerza_maxima

    elif opcion == "min":

        aux_return = fuerza_minima
   
    return aux_return


def sumar_fuerzas_de_heroes_por_genero(lista_personajes:list, genero:str)->float:
     
    aux_suma_fuerzas = 0

    aux_genero = genero.upper()
     
    for heroe in lista_personajes:
        
        if heroe['genero'] == aux_genero:

            aux_suma_fuerzas = aux_suma_fuerzas + int(heroe['fuerza'])

    return aux_suma_fuerzas


def obtener_promedio_fuerzas(aux_suma_fuerzas, aux_cantidad_heroes)->float:
     
    aux_promedio = aux_suma_fuerzas / aux_cantidad_heroes
    
    return aux_promedio

def obtener_valor_de_campo_especifico(lista_personajes, campo:str):

    aux_lista_obtenida = []
    
    for heroe in lista_personajes:

        if type(heroe[campo]) == str:
        
            aux_lista_obtenida.append(heroe[campo].capitalize())

        else:

            aux_lista_obtenida.append(heroe[campo])


    aux_lista_filtrada = set(aux_lista_obtenida)

    return aux_lista_filtrada

def obtener_valor_de_campo_color_pelo(lista_personajes, campo:str):

    aux_lista_obtenida = []
    
    for heroe in lista_personajes:

        if type(heroe[campo]) == str:

            if heroe[campo] == "":

                break
        
            aux_lista_obtenida.append(heroe[campo].capitalize())

        else:

            aux_lista_obtenida.append(heroe[campo])

    aux_lista_filtrada = set(aux_lista_obtenida)

    return aux_lista_filtrada


def imprimir_cantidad_color_ojos(aux_lista_color_ojos, lista_personajes):

    aux_contador = 0

    for color in aux_lista_color_ojos:

        if len(color) == 0:

            aux_color = "sin color"
        
        else:
            
            aux_color = color

        print(f" | {aux_color :^30} | ")

        print("------------------------------------")

        for heroe in lista_personajes:

            if heroe['color_ojos'].capitalize() == aux_color:

                aux_contador = aux_contador + 1

        print(f" | {aux_contador:^30} | ")
        
        aux_contador = 0
        
        print("------------------------------------")
        print("------------------------------------")

def imprimir_cantidad_color_pelo(aux_lista_color_pelo, lista_personajes):

    aux_contador = 0

    for color in aux_lista_color_pelo:

        print(f" | {color :^30} | ")

        print("------------------------------------")

        for heroe in lista_personajes:

            if heroe['color_pelo'] == "":

                heroe['color_pelo'] = "No Hair"


            if heroe['color_pelo'].capitalize() == color:

                aux_contador = aux_contador + 1

        print(f" | {aux_contador:^30} | ")
        
        aux_contador = 0
        
        print("------------------------------------")
        print("------------------------------------")

def imprimir_heroes_por_colores_de_ojo(lista_color_ojos_filtrada, lista_personajes):

    for color in lista_color_ojos_filtrada:

        print(f" | {color :^30} | ")

        print("------------------------------------")

        for heroe in lista_personajes:

            if heroe['color_ojos'].capitalize() == color:

                print(f" | {heroe['nombre']:^30} | ")
        
        print("------------------------------------")
        print("------------------------------------")

def imprimir_heroes_por_inteligencias(aux_lista_inteligencia, lista_personajes):

    for tipo in aux_lista_inteligencia:

        if len(tipo) == 0:

            aux_tipo = "Sin inteligencia"
        
        else:
            
            aux_tipo = tipo

        print(f" | {aux_tipo :^30} | ")

        print("------------------------------------")

        for heroe in lista_personajes:

            if heroe['inteligencia'].capitalize() == aux_tipo:

                 print(f" | {heroe['nombre']:^30} | ")
        
        print("------------------------------------")
        print("------------------------------------")

     
# para tp3

def cargar_lista_auxiliar(lista_personajes, aux_lista_personajes):
    #para hacer mas luego

    pass



def stark_normalizar_datos(lista_personajes, mensaje:str, mensaje_error:str):

    ret = False

    aux_contar_modificiones = 0
    
    if len(lista_personajes) > 0 and lista_personajes != None:

        for heroe in lista_personajes:

            for key in heroe:

                #print(key)

                if not(type(heroe[key]) == int) and not(type(heroe[key]) == float):

                    if re.search("\d+[.]{1}", heroe[key]) != None:
                          
                          heroe[key] = float(heroe[key])

                          ret = True # porque se realizo el cambio de tipo

                          aux_contar_modificiones = aux_contar_modificiones+1

                          #print("\tDato convertido a flotante")

                    elif re.search("\d+", heroe[key]) != None:

                        heroe[key] = int(heroe[key])

                        ret = True # porque se realizo el cambio de tipo

                        aux_contar_modificiones = aux_contar_modificiones+1

                        #print("\tDato convertido a entero")

                    else:

                        #print("No se realizo ningun cambio")

                        ret = False

                else:

                    #print("El dato ya esta normalizado")

                    ret = False

            #print("------------------------------------")
            
    else:

        #la lista, o esta vacia o no existe la lista

        ret = False

    if aux_contar_modificiones > 0:

        ret = True

        print(mensaje)
    
    else:

        ret = False

        print(mensaje_error)


    return ret