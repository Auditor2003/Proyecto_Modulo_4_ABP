# Este módulo contiene la clase GestorClientes.
# Aquí vive la lógica del sistema.
# Main solo llama métodos, pero quien realmente trabaja es el gestor.

# Importamos la clase base Cliente
from clientes.clientes import Cliente

# Importamos las subclases
from clientes.cliente_regular import Cliente_Regular
from clientes.cliente_premium import Cliente_Premium
from clientes.cliente_corporativo import Cliente_Corporativo
from persistencia.cliente_json import guardar_clientes, cargar_clientes



class GestorClientes:
    # Esta clase administra todos los clientes del sistema.
    # Guarda, busca, lista y elimina.

    def __init__(self):
        # Creamos un diccionario para organizar clientes por tipo.
        # Cada tipo tiene su propia lista.
        self._clientes = {
            "regular": [],
            "premium": [],
            "corporativo": []
        }

    def agregar_cliente(self, cliente):
        # Primero verificamos que el objeto realmente sea un Cliente.
        # Si no es un Cliente, no lo aceptamos.

        if not isinstance(cliente, Cliente):   # Ref. Clase 1 ---> animal.py
            print("Error: el objeto no es un Cliente válido.")
            return

        # Antes de agregar, revisamos que no exista otro cliente con el mismo ID.
        if self.buscar_cliente(cliente.get_id()) is not None:
            print("Error: ya existe un cliente con ese ID.")
            return

        # Ahora identificamos qué tipo de cliente es.
        # Según su tipo, lo agregamos a la lista correspondiente.

        if isinstance(cliente, Cliente_Regular):
            self._clientes["regular"].append(cliente)

        elif isinstance(cliente, Cliente_Premium):
            self._clientes["premium"].append(cliente)

        elif isinstance(cliente, Cliente_Corporativo):
            self._clientes["corporativo"].append(cliente)

        else:
            print("Tipo de cliente no reconocido.")
            return

        print("Cliente agregado correctamente.")

    def listar_clientes(self):
        # Primero verificamos si el sistema está completamente vacío.
        # Si todas las listas están vacías, avisamos.
        if all(len(lista) == 0 for lista in self._clientes.values()):
            print("No hay clientes registrados.")
            return

        print("\n=== Listado de Clientes ===")

        # Recorremos cada tipo dentro del diccionario.
        for tipo, lista_clientes in self._clientes.items():

            print(f"Clientes tipo {tipo.capitalize()}:")

            # Si esa lista específica está vacía, lo indicamos.
            if not lista_clientes:
                print("No hay clientes de este tipo.")
                continue

            # Si sí hay clientes, los mostramos uno por uno.
            for cliente in lista_clientes:
                print(cliente)

    def buscar_cliente(self, id_cliente):
        # Este método busca un cliente por su ID.
        # Recorremos todas las listas del diccionario.
        for lista_clientes in self._clientes.values():
            for cliente in lista_clientes:
                if cliente.get_id() == id_cliente:
                    return cliente  # Si lo encuentra, lo devuelve

        # Si termina el recorrido y no encontró nada,
        # devolvemos None.
        return None

    def eliminar_cliente(self, id_cliente):
        # Recorremos todas las listas para buscar el cliente.
        for lista_clientes in self._clientes.values():
            for cliente in lista_clientes:
                if cliente.get_id() == id_cliente:
                    # Si lo encontramos, lo eliminamos.
                    lista_clientes.remove(cliente)
                    print("Cliente eliminado correctamente.")
                    return

        # Si no se encontró en ninguna lista:
        print("Cliente no encontrado.")
