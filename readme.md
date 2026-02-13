## Autor

Diego 
Proyecto desarrollado para el Módulo 4 – ABP  
Gestor Inteligente de Clientes (GIC)

La arquitectura modular permite separar responsabilidades y facilita el mantenimiento y escalabilidad del sistema.

---

## Modelo UML

El diseño se basa en un modelo UML compuesto por:

- Clase base `Cliente`
- Subclases:
  - `Cliente_Regular`
  - `Cliente_Premium`
  - `Cliente_Corporativo`
- Clase `GestorClientes`, encargada de administrar múltiples clientes.

### Relaciones implementadas

- **Herencia:** Las subclases extienden la clase base `Cliente`.
- **Polimorfismo:** Sobrescritura del método `__str__()` en subclases.
- **Composición:** `GestorClientes` contiene múltiples instancias de `Cliente`.

El UML corresponde directamente con la implementación real del sistema.

---

## Aplicación de Programación Orientada a Objetos

### Encapsulación
Los atributos se declaran como protegidos (`_atributo`) y se accede a ellos mediante métodos `get`.

Se reconoce como posible mejora futura la incorporación de métodos `set` para reforzar aún más la encapsulación en procesos de edición.

### Herencia
Las clases `Cliente_Regular`, `Cliente_Premium` y `Cliente_Corporativo` reutilizan la lógica de la clase base mediante `super()`.

### Polimorfismo
Las subclases sobrescriben el método `__str__()` para mostrar información específica según el tipo de cliente.

---

## Validaciones y Manejo de Errores

El sistema implementa:

- Validación de email.
- Excepciones personalizadas:
  - `ClienteError`
  - `ClienteDuplicadoError`
  - `ClienteNoEncontradoError`
  - `ValidacionError`
- Uso de `try-except` en la interfaz principal.
- Registro de eventos mediante la librería estándar `logging`.

Actualmente existe una validación básica en la clase base y una validación centralizada en el módulo `utilidades.validaciones`. Como mejora futura, ambas podrían unificarse para evitar redundancias y fortalecer la coherencia del diseño.

---

## Persistencia de Datos

La información se almacena en un archivo `clientes.json`.

Se implementa:

- Serialización manual de objetos.
- Reconstrucción de objetos según su tipo.
- Manejo de errores en lectura/escritura.
- Uso de la librería estándar `json`.

---

## Pruebas Unitarias

Se desarrollaron pruebas utilizando `unittest` para validar:

- Creación de clientes.
- Validación de descuentos.
- Manejo de duplicados.
- Eliminación de clientes.
- Manejo de excepciones.

Las pruebas permiten verificar el correcto funcionamiento del sistema.

---

## Funcionalidades Principales

- Crear clientes regulares, premium y corporativos.
- Editar clientes.
- Eliminar clientes.
- Listar clientes.
- Validar datos ingresados.
- Persistir información en JSON.
- Registrar actividad del sistema en archivo `gic.log`.

---

## Posibles Mejoras Futuras

- Refuerzo de encapsulación mediante setters.
- Validaciones más avanzadas (por ejemplo, uso de expresiones regulares).
- Mejorar pruebas unitarias.

Estas mejoras permitirían evolucionar el sistema hacia un nivel más profesional sin modificar su arquitectura base.

---


