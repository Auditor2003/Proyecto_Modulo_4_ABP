
# Se encarga de la persistencia de datos, es decir,
# permite guardar y cargar clientes utilizando archivos JSON.

# Uso Json Clase 10 M4 --> Ej. archivo_segro.py - obtener_datos.py
# Uso Json Clase 9 M4 --> leer_datos.py


import json
import os

RUTA_ARCHIVO = "clientes.json"


def guardar_clientes(diccionario_clientes):
    """
    Recibe el diccionario del gestor:
    {
        "10": Cliente_Regular(...),
        "20": Cliente_Premium(...)
    }
    y lo convierte a algo serializable.
    """

    datos_serializables = []

    for cliente in diccionario_clientes.values():

        datos = {
            "tipo": cliente.__class__.__name__,
            "id": cliente.get_id(),
            "nombre": cliente.get_nombre(),
            "email": cliente.get_email(),
            "estado": cliente.get_estado()
        }

        # Si es premium agregamos descuento
        if hasattr(cliente, "_descuento"):
            datos["descuento"] = cliente.get_descuento()

        # Si es corporativo agregamos datos empresa
        if hasattr(cliente, "_razon_social"):
            datos["razon_social"] = cliente._razon_social
            datos["rut_empresa"] = cliente._rut_empresa
            datos["contacto"] = cliente._contacto

        datos_serializables.append(datos)

    try:
        with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
            json.dump(datos_serializables, archivo, indent=4)

    except Exception as e:
        print("Error al guardar los datos:", e)


def cargar_clientes():
    """
    Devuelve una lista de diccionarios con los datos guardados.
    """

    if not os.path.exists(RUTA_ARCHIVO):
        return []

    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    except Exception:
        return []
