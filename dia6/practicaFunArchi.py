from os import system


# Práctica Archivos y Funciones 1
# Crea una función llamada abrir_leer() que abra (open)
# un archivo indicado como parámetro, y devuelva su contenido (read).

archivo=open('prueba.txt','a')
# archivo.write('archivo eliminado')
system("cls")
print("=================...practicando ando...====================\n")
# print(archivo.readlines())

def abrirLeer(archivo):
     contenido=archivo.readlines()
     return contenido



def abrirfor(archivo):
     for t in archivo:
          print(t.rstrip())
     return ''


# print(abrirfor(archivo))



# Crea una función llamada sobrescribir() que abra (open)
# un archivo indicado como parámetro, y sobrescriba cualquier 
# contenido anterior por el texto "contenido eliminado"



def eliminar(archivo):
     archivo.write('archivo eliminado')
     return ''


# print(eliminar(archivo))

# Práctica Archivos y Funciones 3
# Crea una función llamada registro_error() que abra (open) un archivo 
# indicado como parámetro, y lo actualice añadiendo una línea al final que 
# indique "se ha registrado un error de ejecución". Finalmente, debe cerrar el archivo abierto.
 

def registroError(archivo):
  archivo.write('\nse ha registrado un error de ejecucion siii\t')
  archivo.close()
  return ''
  
  
 
 
print(registroError(archivo))

 
 
 
archivo.close()


