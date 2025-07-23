from pathlib import Path



# Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.
# Recuerda importar Path del módulo pathlib, y utilizar el método home()

# ruta base al directorio del usuario
rutabase=Path.home()

# Implementa y crea una ruta relativa que nos permita llegar al archivo 
# "practicas_path.py" a partir de la siguiente estructura de carpetas:
# Almacena el directorio obtenido en la variable ruta. No olvides importar Path.
ruta=Path(rutabase,"cursopython","dia6","practicas_path.py")
print(ruta)