from pathlib import Path, PureWindowsPath

# abrir documento
carpeta= Path('C:/Users/SEDAEDEL/Desktop/proyectos/python/dia6/practica01/practica01.py')

# convertir a ruta windows
rutawindows=PureWindowsPath(carpeta)
print(rutawindows)
# print(carpeta.read_text())
print(carpeta.name)

# TERMONACION O TIPO DE DOCUMENTO
# print(carpeta.suffix)

print(carpeta.stem)
# COPROBAR SI EXISTE EL ARCHIVO

if not carpeta.exists():
    print('no')
else:
    print('si')