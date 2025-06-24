
# =======FRAGMENTAR O HACER SLICING ================

miTexto="Esta es una prueba"
# con indice especifico
resultado=miTexto[5]
# puedo buscar palabras
resultado=miTexto.index("prueba")
# letras
resultado=miTexto.index("p")
# se detiene cuando encuntra lo buscado

# puedo buscar desde inidice determinado
resultado=miTexto.index("a", 3, 8)

# busca de derecha a izquierda con rindex
resultado=miTexto.rindex("p")

print(resultado)