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