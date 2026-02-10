"""
Proyecto Módulo 4 - ABP
Gestor de Clientes 

- Iniciar el programa
- Crear el gestor de clientes
- Llamar a las funciones principales igual que modularización de ABP 3

Se supone que NO contiene lógica de negocio.
Se supone que NO gestiona datos directamente.
"""
# Importamos el gestor de clientes
# El gestor es quien realmente sabe crear, eliminar y listar clientes
# Misma clases referenciadas del ABP 3 ---> Misma Estructura del Control de Stock


# Importamos el gestor de clientes
from gestion_clientes.gestor_clientes import GestorClientes


def main(): # Función principal del programa y se ejecuta al iniciar la aplicación.

    gestor = GestorClientes() # Creamos gestor de clientes donde se almacenarán y administrarán todos los clientes

    print(" Gestor Inteligente de Clientes ")
    
    # Menú Inicial

    while True:
        print("Seleccione una opción:")
        print("1. Agregar cliente (ejemplo)")
        print("2. Listar clientes")
        print("3. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            # Aquí solo se ve el uso del gestor
            print("Funcionalidad de agregar cliente (pendiente de implementación)")

        elif opcion == "2":
            # Aqui va a mostrar los clientes
            gestor.listar_clientes()

        elif opcion == "3":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

# Sin separadores visuales aún, pero ok main