
cantidad_numeros_pares = 0
cantidad_numeros_impares = 0
bandera_primer_numero = True
bandera_primer_par = True
menor_numero = None
mayor_numero = None
menor_numero_par = None
mayor_numero_par = None

for i in range(0,5):

    numero_pedido = input("Ingrese un numero entero: ")

    while (numero_pedido.isalpha() or numero_pedido == 0):

        numero_pedido = input("Ingrese un numero entero valido: ")

    numero_pedido = int(numero_pedido)

    if bandera_primer_numero == True:

        bandera_primer_numero = False
        menor_numero = numero_pedido
        mayor_numero = numero_pedido

    elif numero_pedido < menor_numero:

        menor_numero = numero_pedido

    else:

        mayor_numero = numero_pedido

    if numero_pedido % 2 == 0:

        cantidad_numeros_pares = cantidad_numeros_pares + 1

    else:
    
        cantidad_numeros_impares = cantidad_numeros_impares + 1

    


    



