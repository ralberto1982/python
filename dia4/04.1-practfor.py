# Práctica Loop For 1
# Utilizando loops For, saluda a todos los miembros de una clase,
# imprimiendo "Hola" + su nombre.
# Por ejemplo: "Hola María"
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for alumno in alumnos_clase:
    print(f"Hola {alumno}")

# Práctica Loop For 2
# Dada la siguiente lista de números, realiza la suma de todos los números 
# utilizando loops For y almacena el resultado de la suma en una variable 
# llamada suma_numeros:

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
total=0
for suma in lista_numeros:
    total = total + suma
print(total)



# Práctica Loop For 3
# Dada la siguiente lista de números, realiza la suma de todos los números
# pares e impares* por separado en las variables suma_pares y suma_impares
# respectivamente:

numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
sumaImpares=0
sumaPares=0
for numero in numeros:
    if numero % 2 == 0:
        sumaPares = sumaPares + numero
    else:
         sumaImpares = sumaImpares + numero 
print(sumaPares, sumaImpares)