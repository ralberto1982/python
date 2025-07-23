import os
from pathlib import Path
# leer directorio actual
# ruta=os.getcwd()

#cambiar de  directorio en otra ubicacion
# ruta=os.chdir(r'C:\Users\SEDAEDEL\Desktop\proyectos\python\dia6\practica01')

# crear capeta en un directorio especifico
# ruta=os.makedirs(r'C:\Users\SEDAEDEL\Desktop\proyectos\python\dia6\practica01\\otra')
ruta=r'C:\Users\\SEDAEDEL\\Desktop\\proyectos\\python\\dia6\\practica01\\practica01.py'


# archivo=open('practica01.py')
# print(archivo.readlines())

# rutas divididas
elemento=os.path.basename(ruta)

# nombre del directorio
# elemento=os.path.dirname(ruta)

# mostrar en una tupla
# elemento=os.path.split(ruta)

# eliminar
# elemento=os.rmdir(r'C:\Users\\SEDAEDEL\\Desktop\\proyectos\\python\\dia6\\practica01\\otra')
# elemento=open(r'C:\Users\\SEDAEDEL\\Desktop\\proyectos\\python\\dia6\\practica01\\practica01.py')

# crear rutas que funcionen en cualquier sistema operativo
carpeta=Path(r'C:/Users/SEDAEDEL/Desktop/proyectos/python/dia6/practica01')

# mostrar archivo de la ruta carpeta
archivo=carpeta / 'practica01.py'

miarchivo=open(archivo)

print(miarchivo.read())
