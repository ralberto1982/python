class Pajaro:
    def  __init__(self, color, especie):

        self.color=color
        self.especie=especie

        # methodos
    def piar(self):
        print('pio, mi color es {}'.format(self.color))

    def volar(self,metros):
        print(f"El pajaro ha volado {metros} metros")


# instancias
piolin=Pajaro('rojo','canario')

piolin.piar()
