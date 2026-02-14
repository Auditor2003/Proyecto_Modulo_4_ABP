# Clase base Cliente.
# Es la clase papá del sistema.
# De aquí heredan Regular, Premium y Corporativo.


class Cliente:
    # Clase base donde viven los datos comunes
    # a todos los tipos de clientes.

    # Uso get_variable Ref. Clase 2 Ej. control_precio.py - cuenta_corriente.py

    def __init__(self, id_cliente, nombre, email, estado=True):
        # Constructor base.
        # Guarda la información principal del cliente.

        # Atributos protegidos (convención con _)
        self._id = id_cliente
        self._nombre = nombre
        self._email = email
        self._estado = estado

    def get_id(self):
        # Devuelve el ID del cliente.
        return self._id

    def get_nombre(self):
        # Devuelve el nombre.
        return self._nombre

    def get_email(self):
        # Devuelve el correo.
        return self._email

    def get_estado(self):
        # Indica si está activo o no.
        return self._estado

    def validar_email(self):
        # Validación simple.
        # Solo revisa que tenga un @.
        return "@" in self._email

    def __str__(self):
        # Así se muestra el cliente cuando lo imprimimos.
        estado_texto = "Activo" if self._estado else "Inactivo"
        return f"ID: {self._id} | Nombre: {self._nombre} | Email: {self._email} | Estado: {estado_texto}"

    def __eq__(self, other):
        # Dos clientes son iguales si tienen el mismo ID.
        if not isinstance(other, Cliente):
            return False

        return self._id == other.get_id()

