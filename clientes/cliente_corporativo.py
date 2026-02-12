"""
cliente_corporativo.py

Este módulo contiene la clase ClienteCorporativo.
Representa a un cliente de tipo empresa.
"""

from clientes.cliente import Cliente


class Cliente_Corporativo(Cliente):
    """
    ClienteCorporativo

    Hereda de Cliente y agrega:
    - Razón social
    - RUT de empresa
    - Nombre de contacto
    """

    def __init__(self, id_cliente, nombre, email, razon_social, rut_empresa, contacto, estado=True):
        """
        Constructor de Cliente_Corporativo.

        Parámetros adicionales:
        - razon_social: nombre legal de la empresa
        - rut_empresa: identificador de la empresa
        - contacto: persona de contacto
        """
        super().__init__(id_cliente, nombre, email, estado)
        self._razon_social = razon_social
        self._rut_empresa = rut_empresa
        self._contacto = contacto

    def __str__(self):
        """
        Representación en texto del cliente corporativo.
        Sobrescribe el método de la clase base.
        """
        base = super().__str__()
        return (
            f"{base} | Empresa: {self._razon_social} "
            f"| RUT: {self._rut_empresa} | Contacto: {self._contacto}"
        )
