# Dada la siguiente lista:
# [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
# mostrar el número repetido

lista_numeros = [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]

for i in range(len(lista_numeros)):

    contador_repetidos = 0

    numero_pivote = lista_numeros[i]

    for numero in range(len(lista_numeros)):

        if lista_numeros[numero] == numero_pivote:
            
            contador_repetidos = contador_repetidos + 1

            if contador_repetidos > 1:

                numero_repetido = numero_pivote

print(f"El numero repetido es {numero_repetido}")