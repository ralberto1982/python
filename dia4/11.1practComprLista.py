# ráctica Comprensión de Listas 1
# Para realizar el ejercicio a continuación, puedes optar 
# por diferentes caminos. Si bien en programación el 
# camino correcto es el que devuelve el resultado correcto,
# te animo a que intentes aplicar los conceptos de comprensión
# de listas para comenzar a afianzarlos para el futuro. ¡Pueden 
# resultarte muy útiles en tu práctica profesional!
# Crea una lista valores_cuadrado formada por los
# números de la lista valores, elevados al cuadrado.

valores = [1, 2, 3, 4, 5, 6, 9.5]
temperatura_fahrenheit = [32, 212, 275]

cuadrados=[n ** 2 for n in valores]
# print(cuadrados)



# Práctica Comprensión de Listas 2
# Para realizar el ejercicio a continuación, puedes optar
# por diferentes caminos. Si bien en programación el camino
# correcto es el que devuelve el resultado correcto, te animo
# a que intentes aplicar los conceptos de comprensión de listas
# para comenzar a afianzarlos para el futuro. ¡Pueden resultarte
# muy útiles en tu práctica profesional!
# Crea una lista valores_pares formada por los números de la
# lista valores que (¡adivinaste!) sean pares.

pares=[n for n in valores if n % 2 == 0 ]
# print(pares)


# Práctica Comprensión de Listas 3
# Para realizar el ejercicio a continuación, puedes optar por
# diferentes caminos. Si bien en programación el camino correcto
# es el que devuelve el resultado correcto, te animo a que intentes 
# aplicar los conceptos de comprensión de listas para comenzar 
# a afianzarlos para el futuro. ¡Pueden resultarte muy útiles en
# tu práctica profesional!
# Para la siguiente lista de temperaturas en grados Fahrenheit,
# expresa estos mismos valores en una nueva lista de valores de
# temperatura en grados Celsius. La conversión entre tipo de 
# unidades es la siguiente:
# °C = (°F - 32) * (5/9)

gradoscelcius=[(n - 32) * (5/9) for n in temperatura_fahrenheit]

print(gradoscelcius)
