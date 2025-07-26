# Crea una clase llamada Vehiculo, que contenga los métodos acelerar() y frenar()
# (puedes dejar el código de los métodos en blanco con pass). Crea una clase llamada Automovil 
# que herede estos métodos de Vehiculo.

class Vehiculo:
    pass

    def acelerar(self):
        print('Acelerando')
    
    def frenar(self):
        print('Frenando')


class Automovil(Vehiculo):
    pass


renol=Automovil()

renol.acelerar()
renol.frenar()