"""
Este módulo contiene la clase ClienteRegular.
Sin beneficios especiales.
"""

from clientes.cliente import Cliente


class ClienteRegular(Cliente):
    """
    ClienteRegular

    No agrega nuevos atributos ni comportamientos.
    Utiliza exactamente lo que hereda de Cliente.
    """

    def __init__(self, id_cliente, nombre, email, estado=True):
        """
        Crea ClienteRegular.

        Solo llama al creador de la clase base.
        """
        super().__init__(id_cliente, nombre, email, estado)
