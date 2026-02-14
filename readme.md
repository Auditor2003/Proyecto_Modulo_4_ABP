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


