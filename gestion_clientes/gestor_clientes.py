"""
Este módulo contiene la clase GestorClientes.
Es para administrar los clientes del sistema.

La estructura interna la haré con:
- Un diccionario
- Con listas para cada tipo de cliente

"""

# Importamos la clase base Cliente
from clientes.cliente import Cliente

# Importamos las subclases para poder identificar el tipo
from clientes.cliente_regular import ClienteRegular
from clientes.cliente_premium import ClientePremium
from clientes.cliente_corporativo import ClienteCorporativo

### No se han creado aun las clases ni las fubnciones ### 
### Sólo traigo esquema inicial de ABP 3 ###

class GestorClientes:
    """
    Clase GestorClientes
    Esta clase sólo maneja el sistema
    """

    def __init__(self):
        
        # Para crear el diccionario ---> revisar si la clase es privada o protegida

        self._clientes = {
            "regular": [],
            "premium": [],
            "corporativo": []
        }

        # Aqui ya se agrega un cliente al sistema--->Ver donde se almacena !!!
    def agregar_cliente(self, cliente):
        
        # Validamos que sea un objeto Cliente
        if not isinstance(cliente, Cliente):
            print("Error: el objeto (clase) no es un Cliente válido.")
            return

        # Determinamos el tipo de cliente
        if isinstance(cliente, ClienteRegular):
            self._clientes["regular"].append(cliente)

        elif isinstance(cliente, ClientePremium):
            self._clientes["premium"].append(cliente)

        elif isinstance(cliente, ClienteCorporativo):
            self._clientes["corporativo"].append(cliente)

        else:
            print("Tipo de cliente no reconocido.")
            return

        print("Cliente agregado correctamente.")

    def listar_clientes(self):
        """
        Debería mostrar todos los clientes según su tipo
        """
        """
        Verificar si hay al menos 1 cliente registrado
        Que recorra el diccionario
        Que elimine clientes
        
        """
        