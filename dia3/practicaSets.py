# Práctica Sets 1
# Une los siguientes sets en uno solo, llamado mi_set_3:

s1={1, 2, "tres", "cuatro"}

s2={"tres", 4, 5}

# print(type(s1))
# s3=s1.union(s2)
# print(s3)

# Práctica Sets 2
# Elimina un elemento al azar del siguiente set, 
# utilizando métodos de sets.

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
# al azar
sorteo.pop()
# especifico
sorteo.remove("Camila")
# print(sorteo)


# Práctica Sets 3
# Agrega el nombre Damián al siguiente set,
# utilizando métodos de sets:

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

sorteo.add("Edwin")

print(sorteo)