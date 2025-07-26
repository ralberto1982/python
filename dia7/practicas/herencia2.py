# Crea una clase llamada Mascota, que tenga los siguientes atributos 
# de instancia: edad, nombre, cantidad_patas.
# Crea otra clase, Perro, que herede de la primera sus atributos.


class Mascota:
    def __init__(self,edad,nombre,cantidadPatas):
        self.edad=edad
        self.nombre=nombre
        self.cantidadPatas=cantidadPatas



class Perro(Mascota):
    pass


animal=Perro(2,'firulas',4)


print(animal.cantidadPatas)