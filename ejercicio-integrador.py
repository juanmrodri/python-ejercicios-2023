# La división de higiene está trabajando en un control de stock para productos
# sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de
# contagio, de cada una debe obtener los siguientes datos:

# 1. El tipo (validar "barbijo", "jabón" o "alcohol")
# 2. El precio: (validar entre 100 y 300)
# 3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las
# 1000 unidades)
# 4. La marca y el Fabricante.

# Se debe informar lo siguiente:
# A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
# B. Del ítem con más unidades, el fabricante.
# C. Cuántas unidades de jabones hay en total.

lista_tipos = []
lista_precios = []
lista_unidades = []
lista_marcas = []
lista_fabricantes = []


for i in range(0,5):

    tipo_ingresado = input("Ingrese el tipo de producto (barbijo (b), jabon (j), alcohol (a)): ")

    while not (tipo_ingresado == 'b') and not (tipo_ingresado == 'j') and not (tipo_ingresado == 'a'):

        tipo_ingresado = input("Ingrese el tipo de producto valido (barbijo (b), jabon (j), alcohol (a)): ")
     
    
    precio_ingresado = input("Ingrese el precio del producto (100 y 300): ")

    while not (precio_ingresado.isdigit()):

        precio_ingresado = input("Ingrese un precio valido (100 y 300): ")

    precio_ingresado = float(precio_ingresado)

    while precio_ingresado < 100 or precio_ingresado > 300:
       
       precio_ingresado = input("Ingrese un precio valido entre (100 y 300): ")

       precio_ingresado = float(precio_ingresado)

    
    unidades_ingresadas = input("Ingrese la cantidad de unidades (hasta 1000 unidades): ")

    while not (unidades_ingresadas.isdigit()):

        unidades_ingresadas = input("Ingrese una cantidad de unidades valida (hasta 1000 unidades): ")
            
    unidades_ingresadas = int(unidades_ingresadas)

    while unidades_ingresadas < 1 or unidades_ingresadas > 1000:
         
        unidades_ingresadas = input("Ingrese una cantidad de unidades valida (hasta 1000 unidades): ")

        unidades_ingresadas = int(unidades_ingresadas)

    marca_ingresada = input("Ingrese la marca del producto: ")

    fabricante_ingresado = input("Ingrese el fabricante del producto: ")
    
    lista_tipos.append(tipo_ingresado)     
    lista_precios.append(precio_ingresado)
    lista_unidades.append(unidades_ingresadas)
    lista_marcas.append(marca_ingresada)
    lista_fabricantes.append(fabricante_ingresado)

         

for producto in range(len(lista_tipos)):

    print(lista_tipos[producto])
       


print("carga correcta")