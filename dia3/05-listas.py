# LISTAS VAN ENTRE CORCHETES
# SE PUEDEN INDEXAR
# TIENE METODOS
# LAS LISTAS NO SON INMUTABLES


lista=["A","b","C"]
lista2=[2,"hola", 2.3]
milista3=lista + lista2
# modificar
lista2[0]="edwin"
# fragmentar
print(lista2[1::2])
print("Mi lista tiene ", len(lista), "elemntos")
# concatenar
print(lista2 + lista)
print(lista)

# uniendo
print(" ".join(lista))
# agragando
milista3.append("pedro")
print(milista3)
# eliminando conmetodo pop
lista2.pop()
# mostar elemneto borraso
eliminado=lista.pop()
print(eliminado)
print(lista2)
# ordenar con sort no devuelve nada solo ordena
ordenar=[1,6,7,8,5,4,3,9,10,0]
ordenar.sort()
# ordenar en sentido contrario
ordenar.reverse()
print(ordenar)
