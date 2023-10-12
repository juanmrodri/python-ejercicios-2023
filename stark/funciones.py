
def imprimir_valores(lista_personajes:list):

    print(f"{'Nombre' :^20} | {'identidad' :^30} | {'empresa' :^15} | {'altura' :^20} | {'peso' :^20} | {'genero' :^7} | {'color_ojos' :^25} | {'color_pelo' :^15} | {'fuerza' :^7} | {'inteligencia' :^10}")
            
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    
    for heroe in lista_personajes:

        print(f"{heroe['nombre'] : ^20} | {heroe['identidad']:^30} | {heroe['empresa']:^15} | {heroe['altura']:^20} | {heroe['peso']:^20} | {heroe['genero']:^7} | {heroe['color_ojos']:^25} | {heroe['color_pelo']:^15} | {heroe['fuerza']:^7} | {heroe['inteligencia']:^10}")
    
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

def imprimir_identidad_y_peso(lista_personajes:list, aux_mayor_fuerza):
     
    print(f"{'identidad' :^30} | {'peso' :^20}")
            
    print("---------------------------------------------------------")
    
    for heroe in lista_personajes:

        if int(heroe['fuerza']) == aux_mayor_fuerza:
             
             print(f"{heroe['identidad']:^30} | {heroe['peso']:^20}")
    
    print("---------------------------------------------------------")

def imprimir_nombre_e_identidad(lista_personajes:list, aux_menor_altura):
     
    print(f"{'nombre' :^30} | {'identidad' :^20}")
            
    print("---------------------------------------------------------")
    
    for heroe in lista_personajes:

        if float(heroe['altura']) == aux_menor_altura:

            print(f"{heroe['nombre']:^30} | {heroe['identidad']:^20}")
    
    print("---------------------------------------------------------")

def imprimir_nombre_y_peso_superior_promedio_femenino(lista_personajes:list, aux_promedio_fuerzas_femeninas):
     
    print(f"{'nombre' :^30} | {'peso' :^20}")

    print("---------------------------------------------------------")
   
    for heroe in lista_personajes:
        
        if float(heroe['fuerza']) > aux_promedio_fuerzas_femeninas:
                
            print(f"{heroe['nombre']:^30} | {float(heroe['peso']):.2f}")

    print("---------------------------------------------------------")

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

     
# def obtener_fuerzas_de_heroes(lista_personajes:list, lista_fuerzas:list):

#     for heroe in lista_personajes:

#         if type(heroe['fuerza']) == int:
             
#              lista_fuerzas.append(heroe['fuerza'])

#         elif heroe['fuerza'].isdigit():
             
#             heroe['fuerza'] = int(heroe['fuerza'])

#             lista_fuerzas.append(heroe['fuerza'])
             
#         # if heroe['fuerza'].isdigit():

#         #     heroe['fuerza'] = int(heroe['fuerza'])

#         #     lista_fuerzas.append(heroe['fuerza'])

# def obtener_mayor_fuerza(lista_personajes:list)->int:

#     bandera_primera_vuelta = True

#     for heroe in lista_personajes:

#             if bandera_primera_vuelta == True:

#                 bandera_primera_vuelta = False
#                 fuerza_minima = int(heroe['fuerza'])
#                 fuerza_maxima = int(heroe['fuerza'])

#             elif int(heroe['fuerza']) > fuerza_maxima:

#                 fuerza_maxima = int(heroe['fuerza'])

#             elif int(heroe['fuerza']) < fuerza_minima:

#                 fuerza_minima = int(heroe['fuerza'])
                    
#     return fuerza_maxima

# def cargar_heroes_mayor_fuerza(lista_personajes:list, lista_heroes_mayor_fuerza:list, aux_mayor_fuerza):
     
#      for heroe in lista_personajes:

#                 if heroe['fuerza'] == aux_mayor_fuerza:

#                     lista_heroes_mayor_fuerza.append(heroe)

# def obtener_alturas_de_heroes(lista_personajes:list, lista_alturas:list):

#     for heroe in lista_personajes:
            
#             #falta validar que sean numeros, en este caso, numeros que tengan un . en algun lugar

#             heroe['altura'] = float(heroe['altura'])

#             lista_alturas.append(heroe['altura'])


# def obtener_menor_altura(lista_personajes:list)->float:

#     bandera_primera_vuelta = True

#     for heroe in lista_personajes:

#             if bandera_primera_vuelta == True:

#                 bandera_primera_vuelta = False
#                 altura_minima = float(heroe['altura'])
#                 altura_maxima = float(heroe['altura'])

#             elif float(heroe['altura']) > altura_maxima:

#                 altura_maxima = float(heroe['altura'])

#             elif float(heroe['altura']) < altura_minima:

#                 altura_minima = float(heroe['altura'])
                    
#     return altura_minima

# def cargar_heroes_menor_altura(lista_personajes:list, lista_heroes_menor_altura:list, aux_menor_altura):
     
#      for heroe in lista_personajes:

#                 if heroe['altura'] == aux_menor_altura:

#                     lista_heroes_menor_altura.append(heroe)

# def obtener_peso_de_heroes_masculinos(lista_personajes:list, lista_pesos_masculinos:list):

#     for heroe in lista_personajes:

#         #falta validar que sean numeros, en este caso, numeros que tengan un . en algun lugar

#             heroe['peso'] = float(heroe['peso'])

#             lista_pesos_masculinos.append(heroe['peso'])


# def sumar_pesos_de_heroes_masculinos(lista_personajes:list)->float:
     
#     aux_suma_pesos = 0
     
#     for heroe in lista_personajes:

#         if heroe['genero'] == "M":

#             aux_suma_pesos = aux_suma_pesos + float(heroe['peso'])

#     return aux_suma_pesos


# def contar_cantidad_de_heroes_masculinos(lista_personajes:list)->int:
     
#     aux_contador = 0

#     for heroe in lista_personajes:
        
#         if heroe['genero'] == 'M':
            
#             aux_contador = aux_contador+1

#     return aux_contador

# def obtener_promedio_pesos_masculinos(aux_suma_pesos, aux_cantidad_masculinos)->float:
     
#     aux_promedio = aux_suma_pesos / aux_cantidad_masculinos
    
#     return aux_promedio

# def obtener_fuerza_de_heroes_femeninos(lista_personajes:list, lista_fuerzas_femeninos:list):

#     for heroe in lista_personajes:

#         if type(heroe['fuerza']) == int and heroe['genero'] == "F":
             
#              lista_fuerzas_femeninos.append(heroe['fuerza'])

#         elif heroe['fuerza'].isdigit() and heroe['genero'] == "F":
             
#             heroe['fuerza'] = int(heroe['fuerza'])

#             lista_fuerzas_femeninos.append(heroe['fuerza'])

# def sumar_fuerzas_de_heroes_femeninos(lista_personajes:list)->float:
     
#     aux_suma_fuerzas = 0
     
#     for heroe in lista_personajes:
        
#         if heroe['genero'] == "F":

#             aux_suma_fuerzas = aux_suma_fuerzas + int(heroe['fuerza'])

#     return aux_suma_fuerzas

# def contar_cantidad_de_heroes_femeninos(lista_personajes:list)->int:
     
#     aux_contador = 0

#     for heroe in lista_personajes:
        
#         if heroe['genero'] == 'F':
            
#             aux_contador = aux_contador+1

#     return aux_contador

# def obtener_promedio_fuerzas_femeninas(aux_suma_fuerzas, aux_cantidad_femeninos)->float:
     
#     aux_promedio = aux_suma_fuerzas / aux_cantidad_femeninos
    
#     return aux_promedio