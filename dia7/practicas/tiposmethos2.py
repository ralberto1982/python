# Crea un método de clase revivir() que actúa sobre el atributo de 
# clase vivo de la clase Jugador, estableciéndolo en True cada vez que es invocado.
# El valor predeterminado del atributo vivo, debe ser False.

class Jugador:

    vivo=False
    def __init__(self):
        pass

 
    @classmethod
    def revivir(cls):
        print('El jugador a revivido')
        cls.vivo=True

        
Jugador.revivir()
print(Jugador.vivo)