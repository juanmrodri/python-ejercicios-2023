# Pedir al usuario que ingrese los datos de 5 alumnos y guardarlos en sus
# respectivas listas. Validar el ingreso de datos según su criterio.
# Datos:
# nombre, sexo (f/m), nota (validar).
# Una vez cargados los datos:
# Mostrar el nombre del hombre con nota más baja
# Mostrar el promedio de notas de las mujeres

lista_nombres = []
lista_generos = []
lista_notas = []

for i in range(0,2):

    nombre_pedido = input("Ingrese el nombre: ")

    while nombre_pedido.isdigit():

        nombre_pedido = input("Ingrese un nombre valido: ")

    lista_nombres.append(nombre_pedido)

    genero_pedido =  nombre_pedido = input("Ingrese el genero: ")

    while genero_pedido.isdigit() or (not genero_pedido == "f" and not genero_pedido == "m"):

        genero_pedido = input("Ingrese un genero valido: ")

    lista_generos.append(genero_pedido)

    nota_ingresada = input("Ingrese la nota: ")

    nota_ingresada = int(nota_ingresada)

    while nota_ingresada < 1 or nota_ingresada > 10 :

        nota_ingresada = input("Ingrese una nota valida: ")

        nota_ingresada = int(nota_ingresada)
    
    lista_notas.append(nota_ingresada)
        


for i in range(len(lista_nombres)):

    print(f"nombre: {lista_nombres[i]} - genero: {lista_generos[i]} - nota: {lista_notas[i]}")