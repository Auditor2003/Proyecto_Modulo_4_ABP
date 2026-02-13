# Función simple para validar email

def validar_email(email):

    # Validación muy básica
    # Solo verifica que tenga @ y punto
    if "@" in email and "." in email:
        return True

    return False
