"""

Representa a un cliente con beneficios especiales (descuento)

"""
# Aquí traigo clase padre Cliente
from clientes.cliente import Cliente


class ClientePremium(Cliente):
    """
    Hereda de Cliente y agrega un atributo adicional:
    descuento: % descuento asociado al cliente.
    """

    def __init__(self, id_cliente, nombre, email, descuento, estado=True):
        """
        Creador de la clase ClientePremium.

        Parámetros:
        - id_cliente: identificador único del cliente
        - nombre: nombre del cliente
        - email: correo electrónico del cliente
        - descuento: porcentaje de descuento (entre 0 y 100)
        - estado: indica si el cliente está activo (True por defecto)

        Se llama primero al creador de la clase base (Cliente)
        para inicializar los atributos comunes.
        """

        # Llamamos al creadr de la clase padre (Cliente)
        super().__init__(id_cliente, nombre, email, estado)

        # Verificamos que el descuento sea un número (int o float)
        if not isinstance(descuento, (int, float)):
            raise TypeError("El descuento debe ser un valor numérico.")

        # Verificamos que el descuento esté dentro del rango permitido
        # No puede ser negativo ni mayor a 100%
        if descuento < 0 or descuento > 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")

        # Si pasa las validaciones, se asigna el atributo
        # Usamos self directamente (sin property) para mayor claridad
        self.descuento = descuento

    def __str__(self):
        """
        Traigo datos de la superclase y le agrego descuento encima 
        Indicado por el profe como overwrite
        Sobrescribe el método __str__ de la clase base,
        agregando la información del descuento.
        """

        # Obtenemos la representación base desde la clase padre
        base = super().__str__()
