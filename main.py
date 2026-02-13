# Proyecto Módulo 4 - ABP
# Gestor Inteligente de Clientes
# Este archivo solo controla el programa.
# No maneja datos directamente ni contiene lógica de negocio.

from gestion_clientes.gestor_clientes import GestorClientes


def main():
    # Creamos el gestor.
    # Él es el que sabe realmente cómo trabajar con los clientes.
    gestor = GestorClientes()

    print("Gestor Inteligente de Clientes")

    while True:
        print("Seleccione una opción:")
        print("1. Agregar cliente (demo)")
        print("2. Listar clientes")
        print("3. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            # Aquí solo demostramos cómo se llamaría al gestor.
            # La lógica real debe estar dentro de GestorClientes.
            print("Funcionalidad de agregar cliente aún en construcción.")

        elif opcion == "2":
            # Le pedimos al gestor que muestre los clientes.
            gestor.listar_clientes()

        elif opcion == "3":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

# Esto permite ejecutar el programa directamente
if __name__ == "__main__":
    main()
