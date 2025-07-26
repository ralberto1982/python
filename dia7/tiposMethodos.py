# decoradores
# metodods de instancia

# metodos de clase
# @classmethod

# metodos estaticos
# @staticmethod

class Pajaro:
    alas=True

    def __init__(self, color, especie):
        self.color=color
        self.especie=especie


    def piar(self):
        print('pio')


    def volar(self, metros):
        print(f"El pajaro puede volar {metros} metros")
        self.piar()


    def pintar(self):
        self.color='negro'

        print(f"ahora el pajaro es {self.color}")
    

# piolin=Pajaro('amarillo', 'tuupial')

# # invocar otros metodos ejemplo del methodo volar 
# piolin.volar(50)

# piolin.alas=False

# print(piolin.alas)



# decoradores
# cls=clase
    @classmethod
    def ponerHuevos(cls,cantidad):
        print(f"puso {cantidad} huevos")
        cls.alas=False


# Pajaro.ponerHuevos(3)
# Pajaro.alas
# print(Pajaro.alas)


    @staticmethod
    def mirar():
        print("el pajaro mira")



print(Pajaro.mirar())