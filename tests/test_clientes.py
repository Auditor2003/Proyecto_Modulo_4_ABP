# Este archivo prueba las clases Cliente y sus subclases.

# Bibliografia uso Unittest https://ellibrodepython.com/python-testing#tests-unitarios-en-python-con-unittest
# Apoyo Ingeniero Inf. Italo Muñoz


import unittest

from clientes.clientes import Cliente
from clientes.cliente_premium import ClientePremium


class TestClientes(unittest.TestCase):

    # Probamos creación básica
    def test_creacion_cliente(self):

        cliente = Cliente("1", "Diego", "diego@email.com")

        # Verificamos que el ID sea correcto
        self.assertEqual(cliente.get_id(), "1")

        # Verificamos que el nombre sea correcto
        self.assertEqual(cliente.get_nombre(), "Diego")

    # Probamos validación email
    def test_validar_email(self):

        cliente = Cliente("2", "Ana", "ana@email.com")

        self.assertTrue(cliente.validar_email())

    # Probamos descuento válido
    def test_descuento_valido(self):

        premium = ClientePremium("3", "Luis", "luis@email.com", 20)

        self.assertEqual(premium.get_descuento(), 20)

    # Probamos descuento inválido
    def test_descuento_invalido(self):

        with self.assertRaises(ValueError):
            ClientePremium("4", "Sofia", "sofia@email.com", 150)


# Esto permite ejecutar las pruebas directamente
if __name__ == "__main__":
    unittest.main()