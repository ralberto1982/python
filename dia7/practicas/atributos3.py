class Personaje:
    real=False
    def __init__(self,especie, magico, edad ):
        self.especie=especie
        self.magico=magico
        self.edad=edad



harryPoter=Personaje('Humano','true','25') 

print(harryPoter.edad)