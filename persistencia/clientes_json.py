
# Se encarga de la persistencia de datos, es decir,
# permite guardar y cargar clientes utilizando archivos JSON.

import json
import os

RUTA_ARCHIVO = "clientes.json"


def guardar_clientes(diccionario_clientes):

    datos_serializables = {}

    for tipo, lista_clientes in diccionario_clientes.items():
        datos_serializables[tipo] = []

        for cliente in lista_clientes:
            datos_serializables[tipo].append(cliente.__dict__)

    try:
        with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
            json.dump(datos_serializables, archivo, indent=4)

    except Exception as e:
        print("Error al guardar los datos:", e)


def cargar_clientes():

    if not os.path.exists(RUTA_ARCHIVO):
        return {
            "regular": [],
            "premium": [],
            "corporativo": []
        }

    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    except Exception:
        return {
            "regular": [],
            "premium": [],
            "corporativo": []
        }
