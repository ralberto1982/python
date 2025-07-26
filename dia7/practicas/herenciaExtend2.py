# "El ornitorrinco es una de las criaturas más raras del mundo: aunque es un mamífero,"
# " pone huevos; y amamanta a sus crías pero no tienen mamas." (National Geographic)
# Crea una clase Ornitorrinco que herede de otras clases: Vertebrado, Pez, Reptil, 
# Ave y Mamifero, tal que "construyas" un animal que tiene los siguientes métodos y atributos:
# - poner_huevos()
# - tiene_pico = True
# - vertebrado = True
# - venenoso = True
# - nadar()
# - caminar()
# - amamantar()

class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Pez,Ave,Reptil,Mamifero):
    pass



miOrnitorrinco=Ornitorrinco()
miOrnitorrinco.caminar()
miOrnitorrinco.poner_huevos()
print(miOrnitorrinco.venenoso)