class Mago:

    def __init__(self,magia):
        self.magia=magia


    def lanzarHechizo(self):
        print('Abracadabra')
    

merlin=Mago('espiritual')

merlin.lanzarHechizo()

print(merlin.magia)
