from random import *

# randint me da numeros aleatorios de un rango
# uniform me genera decimales pero lo puedo round para redondearlo 
# ramdon me henera decimales de 0 a 1
# choise me permite trabajar con listas
# shuffle me mescla los numeros
colores=["verde","azul","rojo"]
numeros =list(range(5,50,5))
aleatorio= randint(1, 50)
aleatorio=round(uniform(1,5),1)
aleatorio=random()
aleatorio=choice(colores)

shuffle(numeros)
print(numeros)

print(aleatorio)