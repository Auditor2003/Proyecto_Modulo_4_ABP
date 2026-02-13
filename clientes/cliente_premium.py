# Cliente Premium.
# Tiene un beneficio especial:
# un descuento porcentual.

from clientes.clientes import Cliente


class Cliente_Premium(Cliente):
    # Cliente que tiene descuento.
    # Hereda lo básico y agrega ese beneficio.

    def __init__(self, id_cliente, nombre, email, descuento, estado=True):
        # Constructor del cliente premium.
        # El descuento debe estar entre 0 y 100.

        super().__init__(id_cliente, nombre, email, estado)

        if 0 <= descuento <= 100:
            self._descuento = descuento
        else:
            raise ValueError("El descuento debe estar entre 0 y 100.")

    def get_descuento(self):
        # Devuelve el porcentaje de descuento.
        return self._descuento

    def __str__(self):
        # Mostramos también el descuento.
        base = super().__str__()
        return f"{base} | Descuento: {self._descuento}%"


