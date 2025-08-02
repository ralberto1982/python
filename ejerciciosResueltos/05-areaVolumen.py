from os import system
import math

system("cls")

radio=int(input("Ingrese el Radio: "))
altura=int(input("Ingresa la altura: "))



vol=(math.pi * radio**2) * altura 
area=2 * math.pi * radio**2 * altura


print(f" El area es:{area} \n Volumen es: {vol}")
