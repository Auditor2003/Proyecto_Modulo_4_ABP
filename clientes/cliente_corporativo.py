# Cliente Corporativo.
# Representa una empresa.
# Tiene datos adicionales aparte de los normales.

from clientes.clientes import Cliente

class Cliente_Corporativo(Cliente):
    # Cliente empresa.
    # Agrega razón social, RUT y contacto.

    def __init__(self, id_cliente, nombre, email, razon_social, rut_empresa, contacto, estado=True):
        # Constructor del cliente corporativo.

        super().__init__(id_cliente, nombre, email, estado)

        self._razon_social = razon_social
        self._rut_empresa = rut_empresa
        self._contacto = contacto

    def __str__(self):
        # Muestra la info completa,
        # incluyendo datos de empresa.
        base = super().__str__()
        return (
            f"{base} | Empresa: {self._razon_social} "
            f"| RUT: {self._rut_empresa} | Contacto: {self._contacto}"
        )

