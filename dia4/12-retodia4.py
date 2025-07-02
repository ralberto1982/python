# proyecto del dia 4
from random import randint
"""
 el programa preguntara nombre 
 luego te dira he pensado un numero entre el 1 y el 100 y 
 tienes solo 8 intentos para eliminarlos cual crees que es el numero
 en cada intento el programa respondera4 cosas distitas
 si el numero es menor a 1 y o mayor a 100 le dira que no esta
   dentro del rango
si e numero es menor que el que ha pensado el programa le dira su repuesta es incorrecta
y es menor que el numero secreto
 si es mayor al numero secreto tambien sera incorrecto y mayor
 si el numero es correcto felicitaciones y cuantos intentos a tardado

"""
vidas=0
intento=0
numero=randint(1,100)
nombre=input("Hola, Cual es tu nombre:")


print(f"\n ==============ADIVINA QUE NUMERO TENGO EN MENTE====================\n")
print(f"Hola, {nombre} he pensado un numero  entre el 1 al 100 y tienes 8 intentos para adivinarlo")


while vidas < 8:
    intento=int(input("Cual numero crees que he elegido:"))
    if intento < 0 or intento > 100:
        print(f"Elegiste el numero {intento}, este no puede ser menor a 0 ni mayor a 100")
        print("aun tienes oportunidad")
    elif intento < numero:
        print(f"Elegiste el numero {intento}, este es menor a mi numero")
        print("aun tienes oportunidad")
    elif intento > numero:
        print(f"Elegiste el numero {intento}, este es mayor a mi numero")
        print("aun tienes oportunidad")
    else: 
        print(f"Elegiste el numero {intento}, este es el numero correto")
        print(f"lo hiciste en {vidas} intentos, felicidades")
        break
if intento != numero:
    print(f"Se han agotado los intentos el numero era {numero}")


vidas =vidas + 1    






    


