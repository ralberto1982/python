# herencia
# Dry=don't repeat self

class Animal:

    def __init__(self, edad, color):
        self.edad=edad
        self.color=color
        
    

    def nacer(self):
        print("este animal ha nacido")

    def hablar(self):
        print("este animal emite sonido")




class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
        super.__init__(edad,color)
        self.altura=altura_vuelo
        
        

    def hablar(self):
        print('pio')
    
    def volar(self, metros):
        print(f'el pajaro vuela {metros} metros')



# piolin=Pajaro(2,'red',60)

# piolin.nacer()

# piolin.volar(10)

# print(piolin.color)


# HERENCIA MULTIPLE

class Padre:
    def hablar(self):
        print('hola')

class Madre:
    def reir(self):
        print('ja jajaj')

    def Hablar(self):
        print('Que tal')

class Hijo(Padre,Madre):
    pass


class Nieto(Hijo):
    pass



miNieto=Nieto()

miNieto.hablar()
miNieto.reir()
print(Nieto.__mro__)