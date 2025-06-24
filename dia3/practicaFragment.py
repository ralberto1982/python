# Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:
frase= "Controlar la complejidad es la esencia de la programación"
# Pista: "Controlar" tiene un largo de 9 caracteres.


resultado=frase[:9]

print(resultado)

longi=len(resultado)
print(longi)



# Toma cada tercer caracter empezando desde el
# noveno hasta el final de la frase, e imprime el resultado.

answer="Nunca confíes en un ordenador que no puedas lanzar por una ventana"

resultadoanswer=answer[9::3]
print(resultadoanswer)


# Invierte la posición de todos los caracteres de
# la siguiente frase y muestra el resultado en pantalla.

strin="Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"

reves=strin[::-1]
print(reves)
