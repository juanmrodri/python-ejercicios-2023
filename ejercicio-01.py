#Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su
#sueldo para esa persona.

nombre_pedido = input("Por favor ingrese su nombre: ")

while nombre_pedido.isdigit():

    nombre_pedido = input("Por favor ingrese un nombre valido: ")
    break

sueldo_pedido = input("Por favor ingrese su sueldo: ")

while sueldo_pedido.isalpha():

    sueldo_pedido = input("Por favor ingrese su sueldo valido: ")
    sueldo_pedido = float(sueldo_pedido)
    break

sueldo_pedido = float(sueldo_pedido)

aumento = sueldo_pedido + float(sueldo_pedido) * 0.1

print(f"{nombre_pedido} su sueldo con aumento es $ {aumento}")


