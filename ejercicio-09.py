# Dadas las siguientes listas:
# edades = [25,36,18,23,45]
# nombre = ["Juan","Ana","Sol","Mario","Sonia"]
# y considerando que la posición en la lista corresponde a la misma persona,
# mostar el nombre de la persona más joven

lista_edades = [25,36,18,23,45]

lista_nombre = ["Juan","Ana","Sol","Mario","Sonia"]

bandera_primera_vuelta = True

for edad in range(len(lista_edades)):

    if bandera_primera_vuelta:

        bandera_primera_vuelta = False
        menor_edad = lista_edades[edad]
        mayor_edad = lista_edades[edad]

    elif lista_edades[edad] < menor_edad:

        menor_edad = lista_edades[edad]
        indice_mas_joven = edad

    elif lista_edades[edad] > mayor_edad:

        mayor_edad = lista_edades[edad]


print(f"{lista_nombre[indice_mas_joven]} es la persona mas joven")

        
        
