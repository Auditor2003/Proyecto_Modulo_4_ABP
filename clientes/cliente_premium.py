"""
Tenemos a un cliente con beneficios especiales,
como un descuento porcentual.
"""

# Importamos la clase base Cliente
from clientes.cliente import Cliente


class Cliente_Premium(Cliente):
    """
    Clase Cliente_Premium.
    Hereda de Cliente y agrega un atributo adicional:
    descuento: porcentaje de descuento del cliente.
    """

    def __init__(self, id_cliente, nombre, email, descuento, estado=True):

"""
        Constructor de Cliente_Premium.
        Parámetros:
        - id_cliente: identificador único del cliente
        - nombre: nombre del cliente
        - email: correo electrónico
        - descuento: porcentaje de descuento (0 a 100)
"""
