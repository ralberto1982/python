miset=set([1,2,3])
otroset={1,2,3}
print(len(miset))
print(2 in miset)
print(type(miset))

print(miset)
# unir 
union =miset.union(otroset)
# agregar
otroset.add(4)
# eliminar
otroset.remove(2)
otroset.pop()
# descartar o eliminar un elemnto
otroset.discard(5)
# limpiar un set
otroset.clear()
print(union)
print(otroset)