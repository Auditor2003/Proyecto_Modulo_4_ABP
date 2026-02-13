"""
Según lo indicado por el profe este módulo contiene excepciones personalizadas del sistema y
nos permite manejar errores de forma más profesional.

"""

class ClienteError(Exception):
    
    # Para errores relacionados con clientes.
    
    pass


class ClienteDuplicadoError(ClienteError):
    
    # Se intenta agregar un cliente con un ID que ya existe.
    
    pass


class ClienteNoEncontradoError(ClienteError):
    
    # Cuando no se encuentra un cliente en el sistema.
    
    pass


class ValidacionError(ClienteError):
    
    # Cuando un dato ingresado no cumple con las validaciones del sistema.
    
    pass
