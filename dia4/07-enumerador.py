letras = ['a', 'b', 'c', 'd']
indice=0

# for letra in letras:
#     print(indice, letra)
#     indice += 1


# enumrador
for  letra in enumerate(letras):
    print( letra)
# enumrador con varias variables
for indice, letra in enumerate(letras):
    print(indice, letra)
  
tuplas=list(enumerate(letras))
print(tuplas)

