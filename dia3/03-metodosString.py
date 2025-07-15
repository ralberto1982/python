texto ="este el texto de edwin loaiza"
# matusculas
resultado=texto.upper()
# letra especifica
resultado=texto[1].upper()
# minusculas
resultado=texto.lower()

# separar split
resultado=texto.split()
# con parmetros o criterio
resultado=texto.split("t")
print(resultado)
# join unir
a="aprender"
b="python"
c="es genial"

union=" ".join([a,b,c])


# find encontrar buscar
resultado=texto.find("s")
# arroja -1 cuando hay erro o no lo encuantra
resultado=texto.find("h")

# replacerecibe 2 parametros el texto y el remplazo
resultado=texto.replace("s", "z")



print(union)
print(resultado)

