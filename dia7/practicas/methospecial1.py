# Dada la clase Libro, implementa el método especial __str__ para que cada vez
# que se imprima el objeto, devuelva '"{titulo}", de {autor}'
# (atención: el título debe estar encerrado entre comillas dobles).

class Libro():
    
    def __init__(self, autor, titulo):
        self.autor=autor
        self.titulo=titulo
        
    def __str__(self):
        return f'Titulo:"{self.titulo}" del autor:"{self.autor}" '

miLibro=Libro('juan p','La avestrus mortal')

print(str(miLibro))

