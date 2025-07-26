class Vaca:
    def __init__(self, nombre):
       self.nombre=nombre

    def hablar(self):
        print(self.nombre + "dice muu")


class Abeja:
    def __init__(self, nombre):
       self.nombre=nombre

    def hablar(self):
        print(self.nombre + "dice beee")


vaca1=Vaca('Aurora ')
abeja1=Abeja('lina ')

# vaca1.hablar()
# abeja1.hablar()

# animales=[vaca1, abeja1]

# for animal in animales:
#     animal.hablar()


def animalHabla(animal):
    animal.hablar()


animalHabla(vaca1)
animalHabla(abeja1)
