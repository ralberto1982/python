
# Práctica Min y Max 1
# Obtén el valor máximo entre los valores de la siguiente 
# lista, y almacénalo en una variable llamada valor_maximo:


lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]


# valorMaximo=max(lista_numeros)
# print(valorMaximo)


# Práctica Min y Max 2
# Calcula la diferencia entre el valor máximo y el 
# mínimo en la siguiente lista de números, y almacénalo en una 
# variable llamada rango:

vmin=min(lista_numeros)
vmax=max(lista_numeros)
rango= vmax - vmin
# print(rango)



# Práctica Min y Max 3
# Utilizando max(), min() y métodos de diccionarios, 
# obtén el mínimo valor a partir del siguiente diccionario:
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

edadMin=min(diccionario_edades.values())


# También, obtén el nombre que se ubica último
# en orden alfabético, y almacénalo en una variable 
# llamada ultimo_nombre.

print(max(diccionario_edades))
print(edadMin)
