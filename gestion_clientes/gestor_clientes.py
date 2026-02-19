# Este módulo contiene la clase GestorClientes.
# Aquí vive la lógica del sistema.
# Main solo llama métodos, pero quien realmente trabaja es el gestor.

from clientes.cliente_regular import ClienteRegular
from clientes.cliente_premium import ClientePremium
from clientes.cliente_corporativo import ClienteCorporativo

from utilidades.excepciones import (
    ClienteDuplicadoError,
    ClienteNoEncontradoError,
    ValidacionError
)

from utilidades.validaciones import validar_email
from utilidades.bitacora_de_registros import registrar_evento

from persistencia.clientes_json import guardar_clientes, cargar_clientes


class GestorClientes:

    def __init__(self):

        self._clientes = {}

        datos = cargar_clientes()

        for cliente_data in datos:

            tipo = cliente_data["tipo"]

            if tipo == "ClienteRegular":
                cliente = ClienteRegular(
                    cliente_data["id"],
                    cliente_data["nombre"],
                    cliente_data["email"],
                    cliente_data["estado"]
                )

            elif tipo == "ClientePremium":
                cliente = ClientePremium(
                    cliente_data["id"],
                    cliente_data["nombre"],
                    cliente_data["email"],
                    cliente_data["descuento"],
                    cliente_data["estado"]
                )

            elif tipo == "ClienteCorporativo":
                cliente = ClienteCorporativo(
                    cliente_data["id"],
                    cliente_data["nombre"],
                    cliente_data["email"],
                    cliente_data["razon_social"],
                    cliente_data["rut_empresa"],
                    cliente_data["contacto"],
                    cliente_data["estado"]
                )
            else:
                continue

            self._clientes[cliente.get_id()] = cliente

    # CREAR CLIENTE REGULAR
    def crear_cliente_regular(self, id_cliente, nombre, email):

        if id_cliente in self._clientes:
            raise ClienteDuplicadoError("El cliente ya existe.")

        if not validar_email(email):
            raise ValidacionError("Email inválido.")

        cliente = ClienteRegular(id_cliente, nombre, email)

        self._clientes[id_cliente] = cliente
        guardar_clientes(self._clientes)
        registrar_evento(f"Cliente regular creado: {id_cliente}")

    # CREAR CLIENTE PREMIUM
    def crear_cliente_premium(self, id_cliente, nombre, email, descuento):

        if id_cliente in self._clientes:
            raise ClienteDuplicadoError("El cliente ya existe.")

        if not validar_email(email):
            raise ValidacionError("Email inválido.")

        cliente = ClientePremium(id_cliente, nombre, email, descuento)

        self._clientes[id_cliente] = cliente
        guardar_clientes(self._clientes)
        registrar_evento(f"Cliente premium creado: {id_cliente}")

    # CREAR CLIENTE CORPORATIVO
    def crear_cliente_corporativo(self, id_cliente, nombre, email, razon_social, rut_empresa, contacto):

        if id_cliente in self._clientes:
            raise ClienteDuplicadoError("El cliente ya existe.")

        if not validar_email(email):
            raise ValidacionError("Email inválido.")

        cliente = ClienteCorporativo(
            id_cliente, nombre, email,
            razon_social, rut_empresa, contacto
        )

        self._clientes[id_cliente] = cliente
        guardar_clientes(self._clientes)
        registrar_evento(f"Cliente corporativo creado: {id_cliente}")

    def buscar_cliente(self, id_cliente):
        return self._clientes.get(id_cliente)

    def listar_clientes(self):
        return list(self._clientes.values())

    def eliminar_cliente(self, id_cliente):

        if id_cliente not in self._clientes:
            raise ClienteNoEncontradoError("Cliente no encontrado.")

        del self._clientes[id_cliente]
        guardar_clientes(self._clientes)
        registrar_evento(f"Cliente eliminado: {id_cliente}")

    def editar_cliente(self, id_cliente, nuevo_nombre, nuevo_email):

        if id_cliente not in self._clientes:
            raise ClienteNoEncontradoError("Cliente no encontrado.")

        if not validar_email(nuevo_email):
            raise ValidacionError("Email inválido.")

        cliente = self._clientes[id_cliente]
        cliente._nombre = nuevo_nombre
        cliente._email = nuevo_email

        guardar_clientes(self._clientes)
        registrar_evento(f"Cliente editado: {id_cliente}")