# Dada la siguiente lista:
# [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
# mostrar el mayor.

lista_numeros = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]

numero_mayor = lista_numeros[0]

for i in range(len(lista_numeros)):

    if lista_numeros[i] > numero_mayor:

        numero_mayor = lista_numeros[i]

print(numero_mayor)