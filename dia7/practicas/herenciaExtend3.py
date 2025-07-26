# Un hijo ha heredado de su padre todas sus características, sin embargo, 
# tienen diferentes hobbies. Logra que la clase Hijo herede de Padre todos
# sus métodos y atributos, sobreescribiendo el método hobby() 
# para que se devuelva[1]: "Juego videojuegos en mi tiempo libre"
# [1]: asegúrate de utilizar return seguido de una cadena de texto


class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"

    def reir(self):
        return "Jajaja"
    
    def hobby(self):
        return "Pinto madera en mi tiempo libre"
    
    def caminar(self):
        return "Caminando con pasos largos y rápidos"
        
class Hijo(Padre):
    pass
    


persona=Hijo()
persona.reir()
print(persona.color_ojos)