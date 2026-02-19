# Proyecto Módulo 4 - ABP
# Gestor Inteligente de Clientes
# Este archivo solo controla el programa.
# No maneja datos directamente ni contiene lógica de negocio.


from gestion_clientes.gestor_clientes import GestorClientes


def main():

    gestor = GestorClientes()

    print("Gestor Inteligente de Clientes")

    while True:
        print("Seleccione una opción:")
        print("1. Agregar cliente")
        print("2. Listar clientes")
        print("3. Eliminar cliente")
        print("4. Editar cliente")
        print("5. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            print("Tipo de cliente:")
            print("1. Regular")
            print("2. Premium")
            print("3. Corporativo")

            tipo = input("Tipo: ")

            id_cliente = input("ID: ")
            nombre = input("Nombre: ")
            email = input("Email: ")

            if tipo == "1":
                gestor.crear_cliente_regular(id_cliente, nombre, email)

            elif tipo == "2":
                descuento = float(input("Descuento (%): "))
                gestor.crear_cliente_premium(id_cliente, nombre, email, descuento)

            elif tipo == "3":
                razon_social = input("Razón social: ")
                rut_empresa = input("RUT empresa: ")
                contacto = input("Contacto: ")

                gestor.crear_cliente_corporativo(
                    id_cliente, nombre, email,
                    razon_social, rut_empresa, contacto
                )

            else:
                print("Tipo inválido.")

        elif opcion == "2":
            for c in gestor.listar_clientes():
                print(c)

        elif opcion == "3":
            id_eliminar = input("ID cliente a eliminar: ")
            gestor.eliminar_cliente(id_eliminar)

        elif opcion == "4":
            id_cliente = input("ID a editar: ")
            nombre = input("Nuevo nombre: ")
            email = input("Nuevo email: ")
            gestor.editar_cliente(id_cliente, nombre, email)

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()