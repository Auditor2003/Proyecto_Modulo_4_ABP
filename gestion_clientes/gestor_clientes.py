# Este módulo contiene la clase GestorClientes.
# Aquí vive la lógica del sistema.
# Main solo llama métodos, pero quien realmente trabaja es el gestor.

# Importamos la clase base Cliente
from clientes.clientes import Cliente

# Importamos las subclases
from clientes.cliente_regular import Cliente_Regular
from clientes.cliente_premium import Cliente_Premium
from clientes.cliente_corporativo import Cliente_Corporativo

from persistencia.clientes_json import guardar_clientes, cargar_clientes
from utilidades.excepciones import (
    ClienteDuplicadoError,
    ClienteNoEncontradoError,
    ValidacionError
)

from utilidades.bitacora_de_registros import registrar_evento


class GestorClientes:
    # Esta clase administra todos los clientes del sistema.

    def __init__(self):

        # Cargamos los datos desde JSON
        datos = cargar_clientes()

        self._clientes = {
            "regular": [],
            "premium": [],
            "corporativo": []
        }

        # Reconstruimos objetos Cliente desde los datos cargados
        for tipo, lista in datos.items():

            for datos_cliente in lista:

                if tipo == "regular":
                    cliente = Cliente_Regular(
                        datos_cliente["_id"],
                        datos_cliente["_nombre"],
                        datos_cliente["_email"],
                        datos_cliente["_estado"]
                    )

                elif tipo == "premium":
                    cliente = Cliente_Premium(
                        datos_cliente["_id"],
                        datos_cliente["_nombre"],
                        datos_cliente["_email"],
                        datos_cliente["_descuento"],
                        datos_cliente["_estado"]
                    )

                elif tipo == "corporativo":
                    cliente = Cliente_Corporativo(
                        datos_cliente["_id"],
                        datos_cliente["_nombre"],
                        datos_cliente["_email"],
                        datos_cliente["_razon_social"],
                        datos_cliente["_rut_empresa"],
                        datos_cliente["_contacto"],
                        datos_cliente["_estado"]
                    )

                self._clientes[tipo].append(cliente)

    # CREAR CLIENTES

    def crear_cliente_regular(self, id_cliente, nombre, email):

        cliente = Cliente_Regular(id_cliente, nombre, email)

        if not cliente.validar_email():
            raise ValidacionError("Email inválido.")

        self._agregar_cliente(cliente)

    # MÉTODOS INTERNOS

    def _agregar_cliente(self, cliente):

        if self.buscar_cliente(cliente.get_id()) is not None:
            raise ClienteDuplicadoError("Ya existe un cliente con ese ID.")

        if isinstance(cliente, Cliente_Regular):
            self._clientes["regular"].append(cliente)

        elif isinstance(cliente, Cliente_Premium):
            self._clientes["premium"].append(cliente)

        elif isinstance(cliente, Cliente_Corporativo):
            self._clientes["corporativo"].append(cliente)

        guardar_clientes(self._clientes)
        registrar_evento("Cliente agregado correctamente.")

    # LISTAR

    def listar_clientes(self):

        if all(len(lista) == 0 for lista in self._clientes.values()):
            print("No hay clientes registrados.")
            return

        print("Listado de Clientes")

        for tipo, lista_clientes in self._clientes.items():

            print(f"Clientes tipo {tipo.capitalize()}:")

            if not lista_clientes:
                print("No hay clientes de este tipo.")
                continue

            for cliente in lista_clientes:
                print(cliente)

    # BUSCAR

    def buscar_cliente(self, id_cliente):

        for lista_clientes in self._clientes.values():
            for cliente in lista_clientes:
                if cliente.get_id() == id_cliente:
                    return cliente

        return None

    # ELIMINAR

    def eliminar_cliente(self, id_cliente):

        for lista_clientes in self._clientes.values():
            for cliente in lista_clientes:
                if cliente.get_id() == id_cliente:
                    lista_clientes.remove(cliente)
                    guardar_clientes(self._clientes)
                    registrar_evento("Cliente eliminado correctamente.")
                    return

        raise ClienteNoEncontradoError("Cliente no encontrado.")
