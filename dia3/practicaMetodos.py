# Práctica Métodos de String 1
# Imprime el siguiente texto en mayúsculas, empleando el
frase="método específico de string"

resultado=frase.upper()
print(resultado)


# Práctica Métodos de String 2
# Une la siguiente lista en un string, 
# separando cada elemento con un espacio. Utiliza 
# el método apropiado de listas/strings,
# y muestra en pantalla el resultado.
lista_palabras = ["La","legibilidad","cuenta."]

resultados=" ".join(lista_palabras)
print(resultados)

# ===================================================

# Práctica Métodos de String 3
# Reemplaza en la siguiente frase:
frase= "Si la implementación es dificil de explicar, puede que sea una mala idea."
# los siguientes pares de palabras:
# "difícil" --> "fácil"
# "mala" --> "buena"
# y muestra en pantalla la frase con ambas palabras modificadas.

remplazar=frase.replace("dificil", "facil")
remplazar=remplazar.replace("mala", "buena")
print(remplazar)
