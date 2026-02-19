
# Representa una empresa.
# Tiene datos adicionales aparte de los normales.

from clientes.clientes import Cliente


class ClienteCorporativo(Cliente):

    def __init__(self, id_cliente, nombre, email, razon_social, rut_empresa, contacto, estado=True):

        super().__init__(id_cliente, nombre, email, estado)

        self._razon_social = razon_social
        self._rut_empresa = rut_empresa
        self._contacto = contacto

    def __str__(self):
        base = super().__str__()
        return (
            f"{base} | Empresa: {self._razon_social} "
            f"| RUT: {self._rut_empresa} | Contacto: {self._contacto}"
        )