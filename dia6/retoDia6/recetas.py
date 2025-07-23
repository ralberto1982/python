import os
from pathlib import Path
from os import system 



ruta=Path(Path.home(), "Desktop","proyectos","python","dia6","retoDia6","Recetas")
# ruta=r'C:\Users\\SEDAEDEL\\Desktop\\proyectos\\python\\dia6\\retoDia6\\Recetas'


def contarRecetas(ruta):
    contador=0
    for txt in Path(ruta).glob("**/*.txt"):
        contador=contador + 1
    return contador


def inicio():
    system("cls")
    print("*" * 50)
    print("BIENVENIDO AL ADMINISTRADOR DE RECETAS")
    print("*" * 50)
    print('\n')
    print(f'"LAS RECETAS SE ENCUENTRAN EN: {ruta}')
    print(f'TOTAL RECETAS:{contarRecetas(ruta)}')
    elecion= 'x'

    while not elecion.isnumeric() or int(elecion) not in range(1,7):
        print("ELIGE UNA OPCION:")
        print('''
        [1] -LEER RECETA
        [2] -CREAR RECETA NUEVA
        [3] -CREAR CATEGORIA NUEVA 
        [4] -ELIMINAR RECETA 
        [5] -ELIMINAR  CATEGORIA 
        [6] -SALIR
       
          ''')
        elecion = input()

    return int(elecion)       



def mostrarCategorias(ruta):
    print("CATEGORIAS")
    rutaCategorias=Path(ruta)
    listaCategorias=[]
    contador=1
    for carpeta in rutaCategorias.iterdir():
        carpetaStr= str(carpeta.name)
        print(f"[{contador}] - {carpetaStr}")
        listaCategorias.append(carpeta)
        contador += 1

    return listaCategorias



def elegirCategoria(lista):
    elecionCorrecta = 'x'
    while not elecionCorrecta.isnumeric() or int(elecionCorrecta) not in range(1, len(lista) + 1):
        elecionCorrecta=input("\n Elige una categoria:")
        return lista[int(elecionCorrecta) -1]


def mostrarRecetas(ruta):
    print("Recetas")
    rutaRecetas=Path(ruta)
    listaRecetas=[]
    contador =1

    for receta in rutaRecetas.glob('*.txt'):
        recetaStr = str(receta.name)
        print(f"[{contador}] - {recetaStr}")
        listaRecetas.append(receta)
        contador += 1
    return listaRecetas



def elegirRecetas(lista):
    elecionReceta='x'

    while not elecionReceta.isnumeric() or int(elecionReceta) not in range(1, len(lista) + 1):
        elecionReceta=input("\n Elige una receta:")
    return lista[int(elecionReceta) - 1]




def leerReceta(receta):
    print(Path.read_text(receta))



def crearReceta(ruta):
    existe=False
    while not existe:
        print("Escribe el nombre de tu receta:")
        nombreReceta=input() + '.txt'
        print("Escriba tu nueva receta:")
        contenidoReceta=input()
        rutaNueva=Path(ruta, nombreReceta)

        if not os.path.exists(rutaNueva):
         Path.write_text(rutaNueva,contenidoReceta)
         print(f"Tu receta {nombreReceta} ha sido creada")
         existe=True
        else:
            print("Lo siento la receta ya existe")



def crearCategoria(ruta):
    existe=False
    while not existe:
        print("Escribe el nombre de tu categoria:")
        nombreCategoria=input()
        rutaNueva=Path(ruta, nombreCategoria)

        if not os.path.exists(rutaNueva):
         Path.mkdir(rutaNueva)
         print(f"Tu nueva categoria {nombreCategoria} ha Sido creada")
         existe=True
        else:
            print("Lo siento la categoria ya existe")


def eliminarReceta(receta):
    Path(receta).unlink()
    print(f"la receta {receta.name} ha sido eliminada")

def eliminarCategoria(categoria):
    Path(categoria).rmdir()
    print(f"la categoria {categoria.name} ha sido eliminada")

def volverInicio():
    elecion='x'
    while elecion.lower() != 'v':
     elecion=input("\n presione v para volver al inicio")




finalizarPrograma=False

while not finalizarPrograma:
    menu=inicio()
    if menu ==1:
        misCategorias=mostrarCategorias(ruta)
        micategoria=elegirCategoria(misCategorias)
        misRecetas=mostrarRecetas(ruta)
        miReceta=elegirRecetas(misRecetas)
        leerReceta(miReceta)
        volverInicio()
        

    elif menu == 2:
        misCategorias=mostrarCategorias(ruta)
        micategoria=elegirCategoria(misCategorias)
        crearReceta(micategoria)
        volverInicio()
        
    elif menu ==3:
        crearCategoria(ruta)
        volverInicio()
        
    elif menu == 4:
        misCategorias=mostrarCategorias(ruta)
        micategoria=elegirCategoria(misCategorias)
        misRecetas=mostrarRecetas(ruta)
        miReceta=elegirRecetas(misRecetas)
        eliminarReceta(miReceta)
        volverInicio()
        
    elif menu == 5:
        misCategorias=mostrarCategorias(ruta)
        micategoria=elegirCategoria(misCategorias)
        eliminarCategoria(micategoria)
        volverInicio()
        
    elif menu == 6:
        finalizarPrograma=True