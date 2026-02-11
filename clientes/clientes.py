"""
Este módulo contiene la clase base Cliente.

Representa a un cliente genérico del sistema.
No es un tipo específico de cliente, sino la base
para todos los demás (Regular, Premium, Corporativo).
"""


class Cliente:
    """
    Clase Cliente (clase base)

    Define los atributos y comportamientos comunes
    a todos los tipos de clientes.
    """

    def __init__(self, id_cliente, nombre, email, estado=True):
        """
        Constructor de la clase Cliente.

        Parámetros:
        - id_cliente: identificador único del cliente
        - nombre: nombre del cliente
        - email: correo electrónico
        - estado: indica si el cliente está activo o no
        """

        # Atributos "protegidos"
        # (convención: se acceden desde métodos, no directamente)

        self._id = id_cliente
        self._nombre = nombre
        self._email = email
        self._estado = estado

    
    # Métodos Get (según indicó el profe)
    

    def get_id(self):
        """
        Devuelve el ID del cliente.
        """
        return self._id

    def get_nombre(self):
        """
        Devuelve el nombre del cliente.
        """
        return self._nombre

    def get_email(self):
        """
        Devuelve el email del cliente.
        """
        return self._email

    def get_estado(self):
        """
        Devuelve el estado del cliente (activo / inactivo).
        """
        return self._estado


    # Como funcionan (Comportamiento)


    def validar_email(self):
        """
        Valida de forma simple el email del cliente.

        Esta validación es básica y solo demuestra
        que sabemos dónde ubicar este tipo de lógica.
        """

        return "@" in self._email


    # Métodos específicos 


    def __str__(self):
        """
        Representación en texto del cliente.

        Se utiliza al imprimir el objeto.
        """
        estado_texto = "Activo" if self._estado else "Inactivo"
        return f"ID: {self._id} | Nombre: {self._nombre} | Email: {self._email} | Estado: {estado_texto}"

    def __eq__(self, other):
        """
        Compara dos clientes.

        Dos clientes se consideran iguales
        si tienen el mismo ID.
        """

        if not isinstance(other, Cliente):
            return False

        return self._id == other.get_id()
