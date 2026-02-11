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
        Muestra todos los clientes registrados en el sistema,
        organizados por tipo.
        """

        # Verificamos si hay al menos un cliente registrado
        if all(len(lista) == 0 for lista in self._clientes.values()):
            print("No hay clientes registrados.")
            return

        print("Listado de clientes")

        # Poner Separador visual

        # Recorremos el diccionario de clientes
        for tipo, lista_clientes in self._clientes.items():

            print(f"\nClientes tipo {tipo.capitalize()}:")

        # Poner Separador visual


            # Si no hay clientes de ese tipo, lo indicamos
            if not lista_clientes:
                print("No hay clientes de este tipo.")
                continue

            # Recorremos la lista de clientes del tipo actual
            for cliente in lista_clientes:
                print(cliente)

    def eliminar_cliente(self, id_cliente):
        """
        Elimina un cliente del sistema según su ID.

        Parámetro:
        id_cliente: identificador del cliente a eliminar
        """

        # Recorremos todas las listas del diccionario---> Apoyo Italo
        for lista_clientes in self._clientes.values():
            for cliente in lista_clientes:
                if cliente.id == id_cliente:
                    lista_clientes.remove(cliente)
                    print("Cliente eliminado correctamente.")
                    return

