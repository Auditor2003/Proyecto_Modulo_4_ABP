# Este módulo se encarga de registrar eventos del sistema
# utilizando la librería estándar logging.

# Uso archivos con ext. log - Ref. Clase 9 M4 --> Ej. ejercicio_final.py - metodo_readline.py


import logging

# Configuración básica del log
logging.basicConfig(
    filename="gic.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def registrar_evento(mensaje):
    logging.info(mensaje)
