# manejo de archivos en python open read create  close
# open abrir 
# read leer
# write escribir editar
# podemos aplicar todos lo metodos strings
# no utilizar readline para archivos grandes



# cargamos el archivo
# archivo=open('prueba.txt')
# imprimimos el archivo
# print(archivo.read())

# imprimir una linea
# unaLinea=archivo.readline()
# eliminar espcaciado entre lineas
# print(unaLinea.rstrip())

# podemos utilizar cualquier metodo para strings
# print(unaLinea.upper())

# iterando el archivo
# for l in archivo:
#     print("Aqui dice" + l)


# me las muestra en una lista que puedo manipular
# todas=archivo.readlines()


# MODOS DE APERTURA
# archivo=open('prueba.txt','r')
# archivo=open('prueba.txt','w')
archivo=open('prueba.txt','a')
lista=['una linea','otra linea']
archivo.write('welcome')

for l in lista:
    archivo.writelines(l + '\n')

# archivo.write('soy el nuevo texto')
print(archivo.write('soy el nuevo texto\n'))
print(archivo.write('soy el nuevo texto hola mundo\n'))
print(archivo.writelines(['hola\n', 'de nuevo\n']))


archivo.close()
      








