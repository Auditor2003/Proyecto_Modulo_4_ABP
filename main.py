# Proyecto Módulo 4 - ABP
# Gestor Inteligente de Clientes
# Este archivo solo controla el programa.
# No maneja datos directamente ni contiene lógica de negocio.

from gestion_clientes.gestor_clientes import GestorClientes
from utilidades.excepciones import ClienteError


def main():
    # Creamos el gestor.
    # Él es el que sabe realmente cómo trabajar con los clientes.
    gestor = GestorClientes()

    print("Gestor Inteligente de Clientes")

    while True:
        print("\nSeleccione una opción:")
        print("1. Agregar cliente regular")
        print("2. Listar clientes")
        print("3. Eliminar cliente")
        print("4. Salir")

        opcion = input("Opción: ")

        try:

            if opcion == "1":
                id_cliente = input("ID: ")
                nombre = input("Nombre: ")
                email = input("Email: ")

                gestor.crear_cliente_regular(id_cliente, nombre, email)
                print("Cliente agregado correctamente.")

            elif opcion == "2":
                clientes = gestor.listar_clientes()

                if not clientes:
                    print("No hay clientes registrados.")
                else:
                    print("\nLista de clientes:")
                    for cliente in clientes:
                        print(cliente)

            elif opcion == "3":
                id_cliente = input("ID a eliminar: ")
                gestor.eliminar_cliente(id_cliente)
                print("Cliente eliminado correctamente.")

            elif opcion == "4":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción no válida. Intente nuevamente.")

        except ClienteError as e:
            # Capturamos errores personalizados del sistema
            print("Error:", e)

        except Exception as e:
            # Cualquier otro error inesperado
            print("Error inesperado:", e)


# Esto permite ejecutar el programa directamente
if __name__ == "__main__":
    main()

