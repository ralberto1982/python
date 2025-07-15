archivo=open('texto.txt')
# print(archivo.read())

# unaLinea=archivo.readline()
unaLinea=archivo.readlines()
# print(unaLinea)

for l in archivo:
    print("Aqui dice" + l)


