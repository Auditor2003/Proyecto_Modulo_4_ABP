# Este módulo contiene la clase GestorClientes.
# Aquí vive la lógica del sistema.
# Main solo llama métodos, pero quien realmente trabaja es el gestor.

# Importamos la clase base Cliente
from clientes.clientes import Cliente

# Importamos las subclases
from clientes.cliente_regular import Cliente_Regular
from clientes.cliente_premium import Cliente_Premium
from clientes.cliente_corporativo import Cliente_Corporativo

from utilidades.excepciones import (
    ClienteDuplicadoError,
    ClienteNoEncontradoError,
    ValidacionError
)

from utilidades.validaciones import validar_email
from utilidades.bitacora_de_registros import registrar_evento

from persistencia.clientes_json import guardar_clientes, cargar_clientes


class GestorClientes:

    # Constructor
    def __init__(self):

        # Diccionario donde se almacenan los clientes
        # La clave será el ID
        self._clientes = {}

        # Cargamos datos desde el archivo JSON si existe
        datos = cargar_clientes()

        for tipo, lista in datos.items():

            for cliente_data in lista:

                if tipo == "regular":
                    cliente = Cliente_Regular(
                        cliente_data["id"],
                        cliente_data["nombre"],
                        cliente_data["email"]
                    )

                elif tipo == "premium":
                    cliente = Cliente_Premium(
                        cliente_data["id"],
                        cliente_data["nombre"],
                        cliente_data["email"],
                        cliente_data["descuento"]
                    )

                elif tipo == "corporativo":
                    cliente = Cliente_Corporativo(
                        cliente_data["id"],
                        cliente_data["nombre"],
                        cliente_data["email"],
                        cliente_data["empresa"]
                    )

                self._clientes[cliente.get_id()] = cliente

    
    # CREAR CLIENTE REGULAR
    

    def crear_cliente_regular(self, id_cliente, nombre, email):

        if id_cliente in self._clientes:
            raise ClienteDuplicadoError("El cliente ya existe.")

        if not validar_email(email):
            raise ValidacionError("Email inválido.")

        cliente = Cliente_Regular(id_cliente, nombre, email)

        self._clientes[id_cliente] = cliente

        guardar_clientes(self._clientes)

        registrar_evento(f"Cliente regular creado: {id_cliente}")

    
    # CREAR CLIENTE PREMIUM
    

    def crear_cliente_premium(self, id_cliente, nombre, email, descuento):

        if id_cliente in self._clientes:
            raise ClienteDuplicadoError("El cliente ya existe.")

        if not validar_email(email):
            raise ValidacionError("Email inválido.")

        cliente = Cliente_Premium(id_cliente, nombre, email, descuento)

        self._clientes[id_cliente] = cliente

        guardar_clientes(self._clientes)

        registrar_evento(f"Cliente premium creado: {id_cliente}")

    
    # CREAR CLIENTE CORPORATIVO
    

    def crear_cliente_corporativo(self, id_cliente, nombre, email, empresa):

        if id_cliente in self._clientes:
            raise ClienteDuplicadoError("El cliente ya existe.")

        if not validar_email(email):
            raise ValidacionError("Email inválido.")

        cliente = Cliente_Corporativo(id_cliente, nombre, email, empresa)

        self._clientes[id_cliente] = cliente

        guardar_clientes(self._clientes)

        registrar_evento(f"Cliente corporativo creado: {id_cliente}")

    
    # BUSCAR CLIENTE
    

    def buscar_cliente(self, id_cliente):

        return self._clientes.get(id_cliente)

    
    # LISTAR CLIENTES
    

    def listar_clientes(self):

        return list(self._clientes.values())

    
    # ELIMINAR CLIENTE
    

    def eliminar_cliente(self, id_cliente):

        if id_cliente not in self._clientes:
            raise ClienteNoEncontradoError("Cliente no encontrado.")

        del self._clientes[id_cliente]

        guardar_clientes(self._clientes)

        registrar_evento(f"Cliente eliminado: {id_cliente}")

    
    # EDITAR CLIENTE
    

    def editar_cliente(self, id_cliente, nuevo_nombre, nuevo_email):

        # Verificamos que el cliente exista
        if id_cliente not in self._clientes:
            raise ClienteNoEncontradoError("Cliente no encontrado.")

        # Validamos el nuevo email
        if not validar_email(nuevo_email):
            raise ValidacionError("Email inválido.")

        cliente = self._clientes[id_cliente]

        # Actualizamos los datos
        cliente._nombre = nuevo_nombre
        cliente._email = nuevo_email

        # Guardamos cambios en el archivo JSON
        guardar_clientes(self._clientes)

        registrar_evento(f"Cliente editado: {id_cliente}")


