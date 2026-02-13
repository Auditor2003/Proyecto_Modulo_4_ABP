# Este archivo prueba la clase GestorClientes.

import unittest

from gestion_clientes.gestor_clientes import GestorClientes
from utilidades.excepciones import (
    ClienteDuplicadoError,
    ClienteNoEncontradoError
)


class TestGestorClientes(unittest.TestCase):

    def setUp(self):
        # Se ejecuta antes de cada prueba
        # Creamos un gestor nuevo
        self.gestor = GestorClientes()

    # -------------------------
    # Probamos agregar cliente
    # -------------------------

    def test_agregar_cliente(self):

        self.gestor.crear_cliente_regular("10", "Mario", "mario@email.com")

        cliente = self.gestor.buscar_cliente("10")

        self.assertIsNotNone(cliente)

    # -------------------------
    # Probamos cliente duplicado
    # -------------------------

    def test_cliente_duplicado(self):

        self.gestor.crear_cliente_regular("20", "Laura", "laura@email.com")

        with self.assertRaises(ClienteDuplicadoError):
            self.gestor.crear_cliente_regular("20", "Laura", "laura@email.com")

    # -------------------------
    # Probamos eliminar cliente
    # -------------------------

    def test_eliminar_cliente(self):

        self.gestor.crear_cliente_regular("30", "Pedro", "pedro@email.com")

        self.gestor.eliminar_cliente("30")

        self.assertIsNone(self.gestor.buscar_cliente("30"))

    # -------------------------
    # Probamos eliminar inexistente
    # -------------------------

    def test_eliminar_no_existente(self):

        with self.assertRaises(ClienteNoEncontradoError):
            self.gestor.eliminar_cliente("999")


# Ejecutar pruebas directamente
if __name__ == "__main__":
    unittest.main()
