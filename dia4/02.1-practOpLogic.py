# Práctica Operadores Lógicos 1
# Crea tres variables (num1 ,  num2 y num3):
# Dentro de num1, almacena el valor 36
# Dentro de num2, almacena el resultado de la operación 72/2
# Dentro de num3, almacena el valor 48
# Verifica si num1 es mayor que num2, y menor que num3.
# Almacena el resultado de dicha comparación en una variable 
# llamada mi_bool.

num1=36
num2=72/2
num3=48
miBool= num1 > num2 and num1 < num3


# Práctica Operadores Lógicos 2
# Crea tres variables (num1 ,  num2 y num3):
# Dentro de num1, almacena el valor 36
# Dentro de num2, almacena el resultado de la operación 72/2
# Dentro de num3, almacena el valor 48
# Verifica si num1 es mayor que num2, o menor que num3.
# Almacena el resultado de dicha comparación en una variable
# llamada mi_bool

num1=36
num2=72/2
num3=48
miBool= num1 > num2 or num1 < num3


# Práctica Operadores Lógicos 3
# Verifica si las palabras almacenadas en las siguientes variables:
palabra1 = "exito"
palabra2 = "tecnologia"
# no se encuentran en la frase a continuación, y almacena el resultado de
# esta comprobación (un booleano) en una variable llamada mi_bool:
# "Cuando algo es lo suficientemente importante, lo haces incluso si las
#  probabilidades de que salga bien no te acompañan"
# Elon Musk

frase="Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"

mibool=  ("exito" in frase) and ("tecnologia" in frase)


