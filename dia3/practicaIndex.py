# Encuentra y muestra en pantalla qué caracter 
# ocupa la quinta posición dentro de la siguiente 
# palabra: "ordenador"

word="ordenador"
resultado=word[4]
print(resultado)


# Encuentra y muestra en pantalla el índice de la 
# primera aparición de la palabra "práctica" en la
# siguiente frase:

sentences="En teoría, la teoría y la practica son los mismos, En la practica, no lo son."
resultados=sentences.index("practica")
print(resultados)


# Encuentra y muestra en pantalla el índice de la última
# aparición de la palabra "práctica" en la siguiente frase:

frase= "En teoría, la teoría y la practica son los mismos. En la practica, no lo son"

resultado=frase.rindex("practica")

print(resultado)