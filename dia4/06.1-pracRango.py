# Práctica Rango 1
# Crea una lista formada por todos los números desde
# el 2500 al 2585 (inclusive). Almacena dicha lista en 
# la variable mi_lista.

miLista=list(range(2500,2585))

# print(miLista)


# Práctica Rango 2
# Utilizando la función range(), crea en una única linea de código
# una lista formada por todos los números múltiplos de 3 desde el 3 al 300
# (inclusive). Almacena dicha lista en la variable mi_lista.

lista2=list(range(0,300,50))
# print(lista2)

# Práctica Rango 3
# Utiliza la función range() y un loop para sumar los cuadrados de 
# todos los números del 1 al 15 (inclusive). Almacena el resultado en
#  una variable llamada suma_cuadrados.
# Para ello:
# Crea un rango de valores que puedas recorrer en un loop
# Para cada uno de estos valores, calcula su valor al cuadrado (potencia de 2).
#  Puede que necesites crear variables intermedias (de manera opcional).
# Suma todos los valores al cuadrado obtenidos. Acumula la suma en la variable
#  suma_cuadrados.

sumacuadrados=0

for num in range(1,15):
     if num % 2==0:
          sumacuadrados = sumacuadrados +num
        #   print(num)
print(sumacuadrados)