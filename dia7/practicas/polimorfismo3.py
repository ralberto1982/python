
# Tienes tres clases de personajes en un juego, los cuales cuentan con sus métodos de defensa específicos.
# Crea una función llamada personaje_defender(), 
# que pueda recibir un objeto (una instancia de las clases de tus personajes), y ejecutar su método defender()
# independientemente de qué tipo de personaje se trate.


class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")


miMago=Mago()
miArquero=Arquero()
miSamurai=Samurai( )

def defensa(gerrero):
    gerrero.defender()


defensa(miMago)
defensa(miArquero)
defensa(miSamurai)