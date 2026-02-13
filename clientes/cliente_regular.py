# ClienteRegular.
# No tiene beneficios especiales.
# Es el cliente más básico del sistema.

from clientes.clientes import Cliente


class ClienteRegular(Cliente):
    # Hereda todo de Cliente.
    # No agrega nada nuevo.

    def __init__(self, id_cliente, nombre, email, estado=True):
        # Solo llama al constructor del padre.
        super().__init__(id_cliente, nombre, email, estado)

