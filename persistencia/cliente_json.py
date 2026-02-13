
# Se encarga de la persistencia de datos, decir, permite guardar y cargar clientes
# utilizando archivos en formato JSON.


import json          # Librería estándar para trabajar con JSON
import os            # Permite verificar si existe el archivo


RUTA_ARCHIVO = "clientes.json"



# FUNCIÓN: guardar_clientes


def guardar_clientes(diccionario_clientes):

    # Creamos un nuevo diccionario
    # que contendrá datos (JSON no puede guardar objetos directamente)

    datos_serializables = {}

    # Recorremos cada tipo de cliente (regular, premium, corporativo)
    for tipo, lista_clientes in diccionario_clientes.items():

        # Creamos una lista vacía para ese tipo
        datos_serializables[tipo] = []

        # Recorremos cada objeto cliente
        for cliente in lista_clientes:

            # Convertimos el objeto en diccionario
            # usando __dict__
            # Esto convierte los atributos internos en clave-valor
            datos_serializables[tipo].append(cliente.__dict__)

    # Intentamos guardar el archivo
    try:

        # Abrimos el archivo en modo escritura (w)
        # encoding utf-8 para evitar problemas de caracteres
        with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:

            # json.dump escribe el diccionario en el archivo
            # indent=4 mejora la legibilidad
            json.dump(datos_serializables, archivo, indent=4)

    except Exception as e:
        # Si ocurre cualquier error, lo mostramos en pantalla
        # (más adelante podemos registrar esto en logs)
        print("Error al guardar los datos:", e)


# FUNCIÓN: cargar_clientes


def cargar_clientes():

    # Primero verificamos si el archivo existe
    if not os.path.exists(RUTA_ARCHIVO):

        # Si no existe, devolvemos estructura vacía
        # para que el sistema no se rompa
        return {
            "regular": [],
            "premium": [],
            "corporativo": []
        }

    try:

        # Abrimos el archivo en modo lectura
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:

            # json.load convierte el JSON en diccionario Python
            datos = json.load(archivo)

            return datos

    except json.JSONDecodeError:
        # Si el JSON está mal formado
        print("Error: El archivo JSON está dañado.")

        return {
            "regular": [],
            "premium": [],
            "corporativo": []
        }

    except Exception as e:
        # Cualquier otro error inesperado
        print("Error inesperado al cargar datos:", e)

        return {
            "regular": [],
            "premium": [],
            "corporativo": []
        }
