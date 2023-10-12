import json

def parse_json_stark(path:str)->list:

    archivo = open(path,"r")

    dic_json = json.load(archivo)

    archivo.close()

    return dic_json["heroes"]

lista_heroes = parse_json_stark("archivos\\data_stark.json")

def guardar_csv_stark(path:str, lista:list):

    archivo = open(path,"w")

    for heroe in lista:

        linea = heroe["nombre"] + "," + heroe["identidad"] + "," + heroe["empresa"] + "," + heroe["altura"] + "," + heroe["peso"] + "," + heroe["genero"] + "," + heroe["color_ojos"] + "," + heroe["color_pelo"] + "," + heroe["fuerza"] + "," + heroe["inteligencia"] + "\n"

        archivo.write(linea)

    archivo.close()
    

def parse_csv_stark(path:str)->list:

    with open(path, "r") as archivo:
        
        lista_heroes = []

        for linea in archivo:

            heroe = {}

            lista = linea.split(",")  