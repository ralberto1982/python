# La función incorporada en Python len() tiene un comportamiento polimórfico, ya que calcula el largo de 
# un objeto en función de su tipo 
# (strings, listas, tuples, entre otros), devolviendo la cantidad de items o caracteres que lo componen.
# Crea un iterador que recorra los siguientes objetos: palabra, lista, tupla y muestre en pantalla
# (print()) para cada uno de ellos su longitud con la función len().
# Puedes recordar cómo implementar la función len() siguiente enlace:

palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

def cantidad(palabra):
   letras=0
   for letra in palabra:
        letras+=1
   return letras


def cantidadLista(lista):
   items=0
   for list in lista:
        items+=1
   return items
def cantidadTupla(tupla):
   items=0
   for list in lista:
        items+=1
   return items

coleccion=[palabra,lista,tupla]

for cant in coleccion:
    print(f" tiene {len(cant)} elementos")

print(f"hay {cantidadLista(lista)} items en la lista")
print(f"hay {cantidadTupla(tupla)} items en la tupla")
print(f" la palabra tiene {cantidad(palabra)} de letras ")
print(f"son {len(palabra)} letras en la palabra {palabra}")
