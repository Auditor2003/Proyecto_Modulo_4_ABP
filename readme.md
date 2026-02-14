## Autor

Diego Muñoz Lasanta

Proyecto ABP - Módulo 4

# Gestor Inteligente de Clientes (GIC)

Proyecto desarrollado en Python 3 utilizando Programación Orientada a Objetos (POO).

El sistema permite gestionar distintos tipos de clientes, aplicar validaciones, manejar excepciones personalizadas y almacenar la información en formato JSON.

---

## Estructura del Proyecto

Proyecto_Modulo_4_ABP

--> clientes/  
--> gestion_clientes/  
--> persistencia/  
--> utilidades/  
--> test/  
--> main.py  
--> README.md  

La arquitectura está organizada por módulos para separar responsabilidades y facilitar el mantenimiento.

---

## Modelo del Sistema

El sistema se compone de:

- Clase base Cliente
- Subclases:
  - Cliente_Regular
  - Cliente_Premium
  - Cliente_Corporativo
- Clase GestorClientes que administra múltiples clientes

Se aplican conceptos de:

- Encapsulación
- Herencia
- Polimorfismo
- Manejo de excepciones personalizadas
- Persistencia en JSON
- Registro de eventos con logging

---

## Funcionalidades

- Crear clientes
- Editar clientes
- Eliminar clientes
- Listar clientes
- Validar datos ingresados
- Guardar información en archivo JSON
- Registrar actividad del sistema

---

## Consideraciones Técnicas

- Python 3
- Uso de json
- Uso de logging
- Uso de unittest
- Manejo de try-except

---

## Mejora Proyectada

Como mejora futura, la encapsulación podría reforzarse mediante el uso de métodos set, y la validación de email podría centralizarse completamente para evitar redundancias.

---

## Fuentes bibliográficas Utilizadas

- Uso def __init__() Ref. Clase 2 M4 --> Ej. correo.py -->  # Ref. Clase 1 M4 --> Ej. libro_control_stock.py

- Uso get_variable Ref. Clase 2 Ej. control_precio.py - cuenta_corriente.py

- Uso super()  Ref. Clase 5 M4 --> Ej. herencia_transporte.py

- Uso Json Clase 10 M4 --> Ej. archivo_segro.py - obtener_datos.py

- Uso Json Clase 9 M4 --> leer_datos.py

- Bibliografia uso Unittest https://ellibrodepython.com/python-testing#tests-unitarios-en-python-con-unittest

- Uso archivos con ext. log - Ref. Clase 9 M4 --> Ej. ejercicio_final.py - metodo_readline.py

- Uso Excepciones Ref. Clase 8 --> Ej--> validar.edad.py y Clase 10 --> archivo_seguro.py 

- Uso de Validaciones simples Ref. Clase 7 M4 --> Ej. validar_entrada_numerica.py - jerarquia:errores.py

- Uso try/Except Ref. Clase 7 M4 --> Ej. ejemplo_try_except.py y Clase 10 M4 --> archivo_seguro.py 

- Apoyo Ingeniero Informático Duoc Sr. Italo Muñoz Pomar


