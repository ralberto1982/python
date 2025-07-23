import os
from pathlib import Path
from os import system 



ruta=Path(Path.home(), "Desktop","proyectos","python","dia6","retoDia6","Recetas")
# ruta=r'C:\Users\\SEDAEDEL\\Desktop\\proyectos\\python\\dia6\\retoDia6\\Recetas'



def mostrarRecetas(ruta):
    print("Recetas")
    rutaRecetas=ruta
    listaRecetas=[]
    contador =1

    for receta in rutaRecetas.glob('**/*.txt'):
        recetaStr = str(receta.name)
        print(f"[{contador}] - {recetaStr}")
        listaRecetas.append(receta)
        contador += 1
    return listaRecetas

print(mostrarRecetas(ruta))