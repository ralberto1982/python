"""Los string son inmutables
pueden tener mas de una linea
se pueden multiplicar
hacer saltos d elinea
calcular el largo
"""
# inmutabilidad no pueden ser asignados solo modificados mediante variables
nombre="Carina"
# nombre[0]="K"
print(nombre)

# multiplicar
n1="Kari"
n2="na"
print(n1 * 10)

# saltos de linea UTILIZANDO LAS COMILLAS
poema=""" mil pequenos peces blanco 
como si hirviera el color
del agua"""

print("agua" in poema)
print("sol" not in poema)

# len largo de un string
print(len(poema))