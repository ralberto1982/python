miLista=[1,1,1,1,1,1,1]

print(len(miLista))
print(miLista)


class Objeto():

    pass


miobjeto=Objeto()

# no es posible
# print(len(miobjeto))
# print(miobjeto)




class Cd:
    def __init__(self,autor,titulo,canciones):
        self.autor=autor
        self.titulo=titulo
        self.camciones=canciones

    def __str__(self):
        return f"Albun: {self.titulo} de {self.autor} con {self.camciones} canciones"
    

    def __len__(self):
        return self.camciones
    
    def __del__(self):
        print("se ha eliminado")

miCd=Cd('pink', 'thewall',24)

del miCd
# print(len(miCd))