edad_pedida = input("Ingrese una edad: ")

while (edad_pedida.isalpha() or edad_pedida == 0):

    edad_pedida = input("Ingrese una edad valida: ")

edad_pedida = int(edad_pedida)

estado_civil = input("Ingrese un estado civil (soltero, casado, viudo): ")

while not (estado_civil == "soltero") and not (estado_civil == "casado") and not (estado_civil == "viudo"):

    edad_pedido = input("Ingrese un estado civil valido (soltero, casado, viudo): ")

if (edad_pedida < 18 and not(estado_civil == "soltero")):

    print("Es muy pequeño para NO ser soltero.")