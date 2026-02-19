# Cliente_Regular.
# No tiene beneficios especiales.
# Es el cliente más básico del sistema.

from clientes.clientes import Cliente


class ClienteRegular(Cliente):

    def __init__(self, id_cliente, nombre, email, estado=True):
        super().__init__(id_cliente, nombre, email, estado)
