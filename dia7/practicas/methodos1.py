class Perro:
    def __init__(self, auyar):
         self.auyar=auyar
    
    def ladrar(self):
         print('guau, guau')

pincher=Perro('auuuu')

pincher.ladrar()
print(pincher.auyar)