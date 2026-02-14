# Función simple para validar email

# Uso de Validaciones simples Ref. Clase 7 M4 --> Ej. validar_entrada_numerica.py - jerarquia:errores.py

def validar_email(email):

    # Validación muy básica
    # Solo verifica que tenga @ y punto
    if "@" in email and "." in email:
        return True

    return False
