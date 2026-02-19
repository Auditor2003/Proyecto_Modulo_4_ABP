# Clase base Cliente.
# Es la clase papá del sistema.
# De aquí heredan Regular, Premium y Corporativo.


class Cliente:

    def __init__(self, id_cliente, nombre, email, estado=True):

        self._id = id_cliente
        self._nombre = nombre
        self._email = email
        self._estado = estado

    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_email(self):
        return self._email

    def get_estado(self):
        return self._estado

    def validar_email(self):
        return "@" in self._email

    def __str__(self):
        estado_texto = "Activo" if self._estado else "Inactivo"
        return f"ID: {self._id} | Nombre: {self._nombre} | Email: {self._email} | Estado: {estado_texto}"

    def __eq__(self, other):

        if not isinstance(other, Cliente):
            return False

        return self._id == other.get_id()
